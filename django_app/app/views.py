from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,  'index.html')


def about(request):
    
    return HttpResponse("About")

def contacts(request):
    
    return HttpResponse("contacts")
