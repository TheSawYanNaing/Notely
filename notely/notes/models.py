from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    
    email = models.EmailField(unique=True, null=False, blank=False)
    
    def __str__(self):
        return f"{self.username}"
    
# For notes
class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    category = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    content = models.TextField()

