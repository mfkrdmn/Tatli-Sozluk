from django.shortcuts import render

# Create your views here.

def user_page(request):
    return render(request, 'user_page.html')


def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def contract(request):
    return render(request, "contract.html")