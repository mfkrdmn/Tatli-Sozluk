from django.shortcuts import render,redirect

# Create your views here.

def entry_page(request):
    return render(request, "entry_page.html")


############


def search(request):
    
    if request.method == 'GET':
        searched_entry = request.GET.get['searched_entry']
        
        print(searched_entry)
        
        context = {
            "searched_entry" : searched_entry
        }
        
        return redirect('entrypage')
    
    return render(request, "entry_page.html", context)
