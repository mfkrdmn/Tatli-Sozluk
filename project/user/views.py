from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages, auth
from entry.models import *
# Create your views here.

def user_page(request):
    all_entries = Entry.objects.all()

    my_entries = EntryComments.objects.filter(commented_entry__user=request.user,writer=request.user)

    count_datas = my_entries.count()

    context = {
        'all_entries' : all_entries,
        'my_entries' : my_entries,
        'count_datas' : count_datas
    }
    return render(request, 'user_page.html', context)


############

def login(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("myAccount")

    elif request.method == "POST": #user is not logged in yet
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request, user) 
            messages.success(request, "You are now logged in")
            return redirect("/")

        else:
            messages.error(request, "Invalid login informations")
            return redirect("login")

    
    return render(request, "login.html")



############

def register(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserForm()

        
    context = {
        'form' : form
    }
    return render(request, "register.html",context)

#############


def logout(request):
    auth.logout(request)
    messages.error(request, "You are logged out")
    return redirect("login")

############

def contract(request):
    return render(request, "contract.html")

