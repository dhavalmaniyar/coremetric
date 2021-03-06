from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.
class Comment(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    comment=models.TextField()
    commentedOn= models.DateField(default=timezone.now())

    def __str__(self):
        return self.name + " ("+str(self.commentedOn)+") " 
    
class User(models.Model):
    user=models.TextField(default=None)
    def __str__(self):
        return self.user

class UserCount(models.Model):
    ucount=models.IntegerField()
    def __str__(self):
        return str(self.ucount)