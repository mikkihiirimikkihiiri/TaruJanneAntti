from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=160)
    def __str__(self):
        return str(self.name)



class Feedback(models.Model):
    RATING_CHOICES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Kayttaja")    
    topic = models.ForeignKey("Topic", on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, choices=RATING_CHOICES)
    good = models.TextField(max_length=2000,blank=True )
    bad = models.TextField(max_length=2000,blank=True )
    ideas = models.TextField(max_length=2000,blank=True )
    date =models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return f"{self.date}"

# Create your models here.
