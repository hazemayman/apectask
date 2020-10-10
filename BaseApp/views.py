from django.shortcuts import render
from django.http import HttpResponse , Http404  , JsonResponse , HttpRequest
from django.utils import timezone
from django.shortcuts import render , redirect 
from django.contrib import messages

def HomePage(request):
    print("here")
    return render(request , 'Base/index.html')
def HomePageredirect(request):
    return redirect('/home')
def Requrtiment(request):
    return render(request , 'Base/Requrtiment.html')
def Form(request):
    return render(request , 'Base/form.html')