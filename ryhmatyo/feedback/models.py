from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
class Topic(models.Model):
    name = models.CharField(max_length=200)
    def _str_(self):
        return self.name


class Feedback(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    rating = models.IntegerField(default=50, validators=[MinValueValidator(1),MaxValueValidator(5)])
    good = models.TextField(max_length=2000,blank=True )
    bad = models.TextField(max_length=2000,blank=True )
    ideas = models.TextField(max_length=2000,blank=True )
    date =models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return f"{self.date}"

# Create your models here.
