from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.

def entry_page(request):
    
    if request.method == 'POST':
        searched_entry = request.POST['searched_entry']

        entries = Entry.objects.filter(entry_name__contains=searched_entry)

        entry_comment = EntryComments.objects.filter(commented_entry__entry_name=searched_entry).order_by('-created_at')

        context = {
            "entries" :  entries,
            'searched_entry' : searched_entry,
            'entry_comment' : entry_comment
        }

        return render(request, "entry_page.html", context)

    else:
        context = {
            "entries" :  entries,
        }
        return render(request, "entry_page.html", context)


############


def search(request):

    entries = Entry.objects.all()
   
    context = {

        "entries" :  entries,
    }
    
    return render(request, "entry_page.html", context)


############


def entry_detail(request, pk):

    entries = Entry.objects.all()

    entry_detail = get_object_or_404(Entry, entry_name=pk)

    bring_entry_info = Entry.objects.filter(entry_name=pk)

    entry_comment = EntryComments.objects.filter(commented_entry__entry_name=pk).order_by('-created_at')

    context = {
        'entry_detail' : entry_detail,
        "entries" :  entries,
        'bring_entry_info' : bring_entry_info,
        'entry_comment' :entry_comment,
    }

    return render(request, "entry_detail.html",context )

