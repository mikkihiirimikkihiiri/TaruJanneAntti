from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Feedback
from django.urls.base import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView





#class FeedbackCreateView(CreateView):
   # model=Feedback
    
    #fields = ['author','topic','rating','good','bad','ideas']
    #template_name = "feedback/index.html"
    #succes_url = reverse_lazy('feedback:index')

class FeedbackCreateView(LoginRequiredMixin, CreateView):
    fields = ['topic','rating','good','bad','ideas']
    login_url = '/login/'
    
    model = Feedback
    template_name = 'feedback/index.html'
    succes_url = reverse_lazy('feedback:index')
    #fields = ['comment']
   
    def form_valid(self, form):
        # Set the form's author to the submitter if the form is valid
        form.instance.author = self.request.user
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())
    
