from django.urls import path
from . import views
from .models import Feedback
from django.urls.base import reverse_lazy

app_name = 'feedback'
urlpatterns = [
    #path('', views.index, name='index'),
    path('',views.FeedbackCreateView.as_view(model=Feedback, success_url=reverse_lazy('feedback:index')), name='index'),
    #path('add_message', views.add_message, name='add_message'),
    #path('add_message',views.MessageCreateView.as_view(), name='add_message'),


]