from django.urls import path , include 

from . import views
urlpatterns = [
    # path('' , views.Home , name = 'Home'),
    # path('create/<str:Voltage1>/<str:Current1>/<str:Voltage2>/<str:Current2>/<str:Voltage3>/<str:Current3>/<str:flow1>/<str:flow2>/<str:flow3>/<str:pressure1>/<str:pressure2>/<str:pressure3>/' , views.create , name = 'create' ),
    # path('view/' , views.view , name = 'view'),
    # path('send/' , views.send , name = 'send'),
    # path('retrive/' , views.retrive , name = 'retrive')

    path('home/' , views.HomePage , name = "Home"),
    path('home/Requrtiment/', views.Requrtiment , name = "Requrtiment"),
    path('home/Requrtiment/form/' , include('Forms.urls') , name = 'form')

]
