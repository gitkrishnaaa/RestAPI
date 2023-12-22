from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from accounts.models import Note, CustomUser
from accounts.serializers import NoteSerializer, UserSerializer
from rest_framework.test import APIRequestFactory
from accounts.views import register_user, user_login, user_logout, NoteListCreateView , NoteDetailView, NoteSearchView
from rest_framework.authtoken.models import Token

# Create your tests here.

class NoteModelTest(TestCase):

    def test_create_note(self):
        note = Note.objects.create(title='Test Title', content='Test Content')
        self.assertEqual(note.title, 'Test Title')
        self.assertEqual(note.content, 'Test Content')

    def test_note_str_representation(self):
        note = Note.objects.create(title='Test Title', content='Test Content')
        self.assertEqual(str(note), 'Test Title')

class NoteSerializerTest(TestCase):

    def test_note_serializer(self):
        data = {'title': 'Test Title', 'content': 'Test Content'}
        serializer = NoteSerializer(data=data)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['title'], 'Test Title')
        self.assertEqual(serializer.validated_data['content'], 'Test Content')

class NoteAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        
        self.user = CustomUser.objects.create(username='testuser', password='testpassword')
        #self.token = Token.objects.create(user=self.user)
        Token.objects.create(user=self.user)
        self.note = Note.objects.create(title='Test Title', content='Test Content')

    def test_retrieve_note_authenticated_user(self):
        url = reverse('note-detail', kwargs={'pk': self.note.pk})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Title')
        self.assertEqual(response.data['content'], 'Test Content')

    def test_update_note_authenticated_user(self):
        url = reverse('note-detail', kwargs={'pk': self.note.pk})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        updated_data = {'title': 'Updated Title', 'content': 'Updated Content'}

        response = self.client.put(url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Title')
        self.assertEqual(self.note.content, 'Updated Content')

    def test_delete_note_authenticated_user(self):
        url = reverse('note-detail', kwargs={'pk': self.note.pk})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)

        response = self.client.delete(url)
