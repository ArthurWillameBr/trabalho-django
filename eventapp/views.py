from django.shortcuts import redirect, render, get_object_or_404
from .forms import EventForm
from .models import Event


def eventFormView(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'eventapp/event.html'
    context = {'form': form}
    return render(request, template_name, context)

def showEventView(request):
    obj = Event.objects.all()
    template_name = 'eventapp/show.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def updateEventView(request, id):
    obj = get_object_or_404(Event, id=id)
    form = EventForm(instance=obj)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'eventapp/event.html'
    context = {'form': form}
    return render(request, template_name, context)

def deleteEventView(request, id):
    obj = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'eventapp/confirmation.html'
    context = {'obj': obj}
    return render(request, template_name, context)
