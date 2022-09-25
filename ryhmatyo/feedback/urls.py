from django.urls import path
from . import views

app_name = 'feedback'
urlpatterns = [
    #path('', views.index, name='index'),
    path('',views.FeedbackCreateView.as_view(), name='index'),
    #path('add_message', views.add_message, name='add_message'),
    #path('add_message',views.MessageCreateView.as_view(), name='add_message'),


]