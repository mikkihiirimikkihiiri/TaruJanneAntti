from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Feedback
from django.urls.base import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.generic.edit import CreateView





class FeedbackCreateView(CreateView):
    model=Feedback
    
    fields = ['topic','rating','good','bad','ideas']
    template_name = "feedback/index.html"
    succes_url = reverse_lazy('feedback:index')
