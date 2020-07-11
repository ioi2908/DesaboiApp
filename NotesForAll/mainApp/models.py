from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UploadNotes(models.Model):
    notes = models.FileField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=50)
    
    def __str__(self):
        return self.filename
        
