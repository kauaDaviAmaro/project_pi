from django.shortcuts import render
from .models import Contact

def home(request):
    template = 'home.html'
    return render(request, template)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message)
        contact.save()

    template = 'contact.html'
    return render(request, template)