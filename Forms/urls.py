from django.urls import path , include 

from . import views
urlpatterns = [
    path('' , views.FormFirst , name = "Form"),
    path('second/' ,views.FormSecond , name = 'Form'),
    path('third/',views.FormThird , name='Form'),
    path('saved/',views.SaveData , name= 'save data')
]
