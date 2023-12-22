
from django.urls import path
from .views import register_user, user_login, user_logout, NoteListCreateView , NoteDetailView, NoteSearchView, NotesharehView

urlpatterns = [
    path('auth/signup/', register_user, name='register'),
    path('auth/login/', user_login, name='login'),
    path('auth/logout/', user_logout, name='logout'),
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/',NoteDetailView.as_view(), name='note-detail'),
    path('search/',NoteSearchView.as_view(), name='note-search'),
    path('notes/<int:pk>/share/',NotesharehView.as_view(), name='share'),
]