from django.shortcuts import render
from .models import Event

def home(request):
    template = 'events.html'
    events = Event.objects.all()
    return render(request, template, {'events': events})