from django.shortcuts import render
from django.http import HttpResponse , Http404  , JsonResponse , HttpRequest
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import render , redirect 
from django.contrib import messages
from . import forms
from . import models

# Create your views here.

def FormFirst(request):
    FormFirst.data = None
    if(request.method == 'POST'):
        # print(request.POST)
        form = forms.FirstPage(request.POST)
        if(form.is_valid()):
            FormFirst.data = form.cleaned_data
            return redirect("/home/Requrtiment/form/second/" , data = form.cleaned_data)
         
    else:
        form = forms.FirstPage()
    return render(request , 'forms/form.html' , {'form' : form})

def FormSecond(request):
    FormSecond.data = None
    print(FormFirst.data)
    if(request.method == 'POST'):
        # print(request.POST)
        form = forms.SecondPage(request.POST)
        if(form.is_valid()):
            FormSecond.data = form.cleaned_data
            return redirect("/home/Requrtiment/form/third/" )
    else:
        form = forms.SecondPage()
    return render(request , 'forms/form.html' , {'form' : form ,'second' : 'second'})


def FormThird(request):
    FormThird.data = None
    if(request.method == 'POST'):
        # print(request.POST)
        form = forms.ThirdPage(request.POST)
        if(form.is_valid()):
            FormThird.data = form.cleaned_data
            return redirect("/home/Requrtiment/form/saved/")

    else:
        form = forms.ThirdPage()
    return render(request , 'forms/form.html' , {'form' : form , 'third' : 'third'})

def SaveData(request):
    application = models.Application(Name = FormFirst.data['Name'],
      MobileNumber = FormFirst.data['MobileNumber'],
      Univesity = FormFirst.data['Univesity'],
      Faculty = FormFirst.data['Faculty'],
      Academic_year = FormFirst.data['Academic_year'],
      First_preference = FormFirst.data['First_preference'],
      Second_preference = FormFirst.data['Second_preference'],
      Previous_experience = FormFirst.data['Previous_experience'],
      Whyapec = FormSecond.data['Whyapec'],
      Hear = FormSecond.data['Hear'],
      First_second_pref = FormSecond.data['First_second_pref'],
      Percentage = FormSecond.data['Percentage'],
      Expect = FormSecond.data['Expect'],
      PersonalSkills = FormSecond.data['PersonalSkills'],
      ALone_team = FormThird.data['ALone_team'],
      Schedule = FormThird.data['Schedule'],
      Learn = FormThird.data['Learn'],
      LeaderRadio = FormThird.data['LeaderRadio'],
      LeaderChar = FormThird.data['LeaderChar'],
      )
    application.save()
    return render(request , 'forms/thanks.html')

