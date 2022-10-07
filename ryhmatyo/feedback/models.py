from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Count









class Feedback(models.Model):
    author = models.ForeignKey(User, null=True,blank=True,on_delete=models.CASCADE)
    RATING_CHOICES = (
        
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        )
    topic = models.ForeignKey("Topic", on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, choices=RATING_CHOICES)
    good = models.TextField(max_length=2000,blank=True )
    bad = models.TextField(max_length=2000,blank=True )
    ideas = models.TextField(max_length=2000,blank=True )
    date =models.DateTimeField(auto_now_add=True)
    class Meta:
       
        unique_together = [['author', 'topic']]
   

    def __str__(self):
        return str(self.topic)

    
class Topic(models.Model):
   
   name = models.CharField(max_length=160)
   def __str__(self):
        return str(self.name)















  

# Create your models here.
