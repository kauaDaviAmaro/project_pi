from django.shortcuts import render
from .models import Event

def home(request):
    template = 'events.html'
    return render(request, template)

def create_event(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        date = request.POST.get('date')
        time = request.POST.get('time')

        event = Event(name=name, description=description, date=date, time=time)
        event.save()
        return render(request, 'events.html')
    template = 'create_event.html'
    return render(request, template)
