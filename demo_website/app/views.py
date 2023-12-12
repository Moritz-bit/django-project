from django.shortcuts import render, HttpResponse
import random

from .forms import CheckinForm

# Create your views here.
def home(request):
    return render(request, "home.html",{})

def checkin(request):
    if request.method == 'POST':
        form = CheckinForm(request.POST)
        if form.is_valid():
            values = list(form.cleaned_data.values())
            if False in values:
                form = CheckinForm(initial=form.cleaned_data)
                form.submit_msg=""  
            else:
                #not all of the SBD can run good simultaneously
                random.seed()
                i = random.choice(['squatcheckbox', 'benchcheckbox', 'deadliftcheckbox'])
                form.cleaned_data[i] = False
                form = CheckinForm(initial=form.cleaned_data)
    else:
        form = CheckinForm
    return render(request, "checkin.html",{'form': form})

def snake(request):
    return render(request, "snake.html",{})

def action(request):
    return render(request, "action.html",{})
