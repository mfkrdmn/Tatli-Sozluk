from django.shortcuts import render,redirect
from entry.models import *
# Create your views here.

def home(request):
    entries = Entry.objects.all()

    context = {
        'entries' : entries
    }
    return render(request, 'home.html', context)


