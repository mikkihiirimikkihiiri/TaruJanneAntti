from pydoc_data.topics import topics
from unicodedata import name
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import BaseFormView, CreateView
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.db.models import Count,Avg

from feedback.models import Feedback
from feedback.models import Topic
from .models import Post
from django.db.models import Sum


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea
        }

class PostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = PostForm
    model = Post
    template_name = 'guestbook/post.html'
    #fields = ['comment']
    success_url = reverse_lazy('guestbook:index')
    def form_valid(self, form):
        # Set the form's author to the submitter if the form is valid
        form.instance.author = self.request.user
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())




# Create your views here.
def index(request):
    questions = Topic.objects.annotate(number_of_answers=Sum('feedback__rating'))
    ratin_sum = Topic.objects.annotate(number_of_answers1=Count('feedback'))
    
    e=0
    v=[]
    while e<len(questions):
        if(ratin_sum[e].number_of_answers1==0):
            v.append({questions[e].name,0})
            e=e+1
        else:
        
            v.append({questions[e].name,questions[e].number_of_answers/ratin_sum[e].number_of_answers1})
            e=e+1
    #q=Feedback.objects.values('topic').annotate(average_rating=Avg('author__feedback'))
    #a= Feedback.objects.aggregate(Sum('rating'))
    #print(a)
    #questions= Feedback.objects.annotate(avg_rating=Avg('topic__feedback')).order_by('-avg_rating')
    return render(request,'guestbook/index.html', {
            'v':v})
    