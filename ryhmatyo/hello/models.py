from django.db import models

class Message(models.Model):
    message_text = models.CharField(max_length=160)
    date = models.DateTimeField('date created', auto_now_add=True)
    def __str__(self):
        return self.message_text


# Create your models here.

