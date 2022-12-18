from django.shortcuts import render,get_object_or_404,redirect
from .models import *

# Create your views here.

def entry_page(request):

    if 'search_entry_button' in request.POST:

        global searched_entry

        searched_entry = request.POST['searched_entry']

        global entry_found

        entry_found = Entry.objects.filter(entry_name__contains=searched_entry)

        global entry_comment

        entry_comment = EntryComments.objects.filter(commented_entry__entry_name=searched_entry).order_by('-created_at')
    
        global all_entries

        all_entries = Entry.objects.all()


    if  entry_found:

        if 'new_comment_searched_entry_button' in request.POST:

            entry_detail = get_object_or_404(Entry, entry_name=searched_entry)
        
            #add comment if new_comment_searched_entry in request.POST:
    
            comment_body = request.POST['comment_body']
            new_comment = EntryComments.objects.create(commented_entry=entry_detail, comment_body=comment_body)
            new_comment.save()

            #show datas if new_comment_searched_entry in request.POST:

            entry_found = Entry.objects.filter(entry_name__contains=searched_entry)
            all_entries = Entry.objects.all()
            entry_comment = EntryComments.objects.filter(commented_entry__entry_name=searched_entry).order_by('-created_at')

    else:

        if 'new_entry_not_in_database' in request.POST:
            entry_name = searched_entry
            new_entry = Entry.objects.create(entry_name=entry_name, user=request.user)
            new_entry.save()
            entry_found = entry_name
            all_entries = Entry.objects.all()

            context = {
                'searched_entry' : searched_entry,
                "entry_found" :  entry_found,
                'entry_comment' : entry_comment,
                "all_entries" :all_entries
            }

            return render(request, "entry_page.html", context)

        if 'not_today_button' in request.POST:
            return redirect("home")
            

    context = {
        'searched_entry' : searched_entry,
        "entry_found" :  entry_found,
        'entry_comment' : entry_comment,
        "all_entries" :all_entries
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

