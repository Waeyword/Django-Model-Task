
# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author =models.ForeignKey(User, on_delete=models.CASCADE) 
    created_on = models.DateTimeField(auto_now=True)
    text = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

class Meta:
    ordering = ('-created_on')

def __str__(self):
    return self.title