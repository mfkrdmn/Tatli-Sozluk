from django.shortcuts import render,get_object_or_404
from .models import *

# Create your views here.

def entry_page(request):
    
    if request.method == 'POST':
        searched_entry = request.POST['searched_entry']

        entry_found = Entry.objects.filter(entry_name__contains=searched_entry)

        entry_comment = EntryComments.objects.filter(commented_entry__entry_name=searched_entry).order_by('-created_at')
        all_entries = Entry.objects.all()

        if not entry_found:

            entry_name = searched_entry

            new_entry = Entry.objects.create(entry_name=entry_name, user=request.user)
            new_entry.save()

        context = {
            "entry_found" :  entry_found,
            'searched_entry' : searched_entry,
            'entry_comment' : entry_comment,
            "all_entries" :all_entries
        }

        return render(request, "entry_page.html", context)

    else:
        all_entries = Entry.objects.all()

        context = {
            "entry_found" :  entry_found,
            "all_entries" :all_entries
        }
        return render(request, "entry_page.html", context)


############


def search(request):

    all_entries = Entry.objects.all()
   
    context = {

        "all_entries" :  all_entries,
    }
    
    return render(request, "entry_page.html", context)


############


def entry_detail(request, pk):

    all_entries = Entry.objects.all()

    entry_detail = get_object_or_404(Entry, entry_name=pk)

    bring_entry_info = Entry.objects.filter(entry_name=pk)

    entry_comment = EntryComments.objects.filter(commented_entry__entry_name=pk).order_by('-created_at')

    
    if request.method == "POST":
        comment_body = request.POST['comment_body']

        new_comment = EntryComments.objects.create(commented_entry=entry_detail, comment_body=comment_body)
        new_comment.save()

 

    context = {
        'entry_detail' : entry_detail,
        "all_entries" :  all_entries,
        'bring_entry_info' : bring_entry_info,
        'entry_comment' :entry_comment,
    }

    return render(request, "entry_detail.html",context )

