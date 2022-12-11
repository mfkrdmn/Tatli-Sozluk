from django.shortcuts import render,redirect
from entry.models import *
# Create your views here.

def home(request):
    all_entries = Entry.objects.all()

    context = {
        'all_entries' : all_entries
    }
    return render(request, 'home.html', context)


