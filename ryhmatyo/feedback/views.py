from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Feedback
from django.urls.base import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count

from feedback.models import Feedback
from feedback.models import Topic

from django.db.models import Sum






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

def index1(request):
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
    return render(request,'feedback/index1.html', {
            'v':v})
    
    
