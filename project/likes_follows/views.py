from django.shortcuts import render
from.models import *
from entry.models import *
# Create your views here.

def users_liked_comments(request):

    all_entries = Entry.objects.all()

    for i in EntryComments:
        comments = i.likes_to_the_comment

    a = comments + 1
        

    context = {
        'all_entries' : all_entries,
        'a' : a
    }

    return render(request, "liked_comments.html", context)

