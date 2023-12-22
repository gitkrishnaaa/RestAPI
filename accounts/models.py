from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.

#User model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    # Add custom fields here, if needed

    def __str__(self):
        return self.username 

#Notes model


class Note(models.Model):
    title = models.CharField(max_length=255,  db_index=True,)
    content = models.TextField(db_index=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    shared_to = models.JSONField(default=list)

    def __str__(self):
        return self.title
     