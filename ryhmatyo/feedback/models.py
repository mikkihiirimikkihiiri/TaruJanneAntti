from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=160)
   
    def _str_(self):
        return self.name
    




class Feedback(models.Model):
    RATING_CHOICES = (
        
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        )
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, choices=RATING_CHOICES)
    good = models.TextField(max_length=2000,blank=True )
    bad = models.TextField(max_length=2000,blank=True )
    ideas = models.TextField(max_length=2000,blank=True )
    date =models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return f"{self.date}"

# Create your models here.
