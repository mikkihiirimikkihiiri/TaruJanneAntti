from django.urls import path
from . import views
from .models import Message
from django.urls.base import reverse_lazy

app_name = 'hello'
urlpatterns = [
    #path('', views.index, name='index'),
    path('',views.IndexView.as_view(), name='index'),
    #path('add_message', views.add_message, name='add_message'),
    path("add_message",views.MessageCreateView.as_view(model=Message, success_url=reverse_lazy('hello:index')), name='add_message'),


]