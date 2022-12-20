from django.shortcuts import render,redirect,get_object_or_404
from entry.models import *
# Create your views here.

def home(request):
    all_entries = Entry.objects.all().order_by('-created_at')
    first_comment = EntryComments.objects.all().order_by('-created_at')

    context = {
        'all_entries' : all_entries,
        'first_comment' :first_comment,
    }
    return render(request, 'home.html', context)


