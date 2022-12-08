from django.shortcuts import render,redirect
# Create your views here.

def project_flow(request):
    return render(request,"project_flow.html")