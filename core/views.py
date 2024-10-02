from django.shortcuts import render
from .models import Contact
import datetime

def home(request):
    """View for the home page."""
    year = datetime.date.today().year
    context = {"year": year}
    return render(request, "home.html", context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message)
        contact.save()

    template = 'contact.html'
    return render(request, template)

def about(request):
    template = 'about.html'
    return render(request, template)