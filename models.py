from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    
   
    
class Note(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE,)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=(('text', 'Text'), ('audio', 'Audio'), ('video', 'Video')))

