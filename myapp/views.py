from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello_say(request):
    return HttpResponse("Hello, world!")
# def homepage(request):
#     return HttpResponse("This is the homepage of my Django app!")

def homepage(request):
    return render(request, 'index.html')
def about(request):

    return render(request, 'about.html', {'about': about_us, 'contact': contact_us })
    
def contact(request):
    context = {
        'page_title': 'Contact Us',
        'contact_email': 'support@example.com',
       'contact_phone': '123-456-7890',
        'services': ['Web Development', 'SEO', 'Consulting'],
        'business_hours': {
            'Monday-Friday': '9 AM - 5 PM',
            'Saturday': '10 AM - 2 PM',
            'Sunday': 'Closed'
        }

    }
    return render(request, 'contact.html', context)