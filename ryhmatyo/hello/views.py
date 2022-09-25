from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Message
from .forms import MessageForm

#def index(request):
 #   context = {"latest_message_list": Message.objects.order_by('-date')[:10]}
  #  return render(request, 'hello/index.html', context)
class IndexView(ListView):
    template_name = 'hello/index.html'
    context_object_name = 'latest_message_list'
    def get_queryset(self):
        return Message.objects.order_by('-date')[:10]
class MessageCreateView(CreateView):
    model = Message
    fields = ['message_text']
    template_name = "hello/add_page.html"
    succes_url = reverse_lazy('hello:index')

def add_message(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MessageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            message_text = request.POST["message_text"]
            message = Message(message_text =message_text)
            message.save()
            
            # save to dictionary
            
            
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('hello:index'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = MessageForm()
    return render(request, 'hello/add_page.html', {'form': form})
  

