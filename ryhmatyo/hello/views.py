from django.shortcuts import render

def index(request):
    context = {"age":25,"firstname":"antti"}
    return render(request, 'hello/index.html', context)
def second(request):
    context = {}
    return render(request, 'hello/second.html', context)
