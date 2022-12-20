from django.shortcuts import render,redirect,get_object_or_404
from entry.models import *
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    all_entries = Entry.objects.all().order_by('-created_at')
    first_comment = EntryComments.objects.all().order_by('-created_at')

    #Paginator


    paginator = Paginator(first_comment, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    #

    context = {
        'all_entries' : all_entries,
        'page_obj': page_obj
    }
    return render(request, 'home.html', context)


