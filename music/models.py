from django.db import models

# Create your models here.

class Song_data(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to="img")
    audio=models.FileField(upload_to="audio")

    def __str__(self):
        return self.title

    class Meta:
        ordering=['title']