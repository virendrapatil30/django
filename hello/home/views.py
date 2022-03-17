from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
   # return HttpResponse("Hi Django")
    context = {
       'variable':"This is from variable",
        'variable1': "This is from variable1"
    }
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):

    return render(request, 'contact.html')