from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def hello_say(request):
    return HttpResponse("Hello, world!")
# def homepage(request):
#     return HttpResponse("This is the homepage of my Django app!")

def homepage(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')  
