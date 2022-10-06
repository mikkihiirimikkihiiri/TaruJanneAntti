from django.urls import path

from . import views

app_name = 'average'
urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.PostView.as_view(), name='post'),
]
