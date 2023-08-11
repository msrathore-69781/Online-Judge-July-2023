from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   # path("home/",views.problem,name="problem get")
   path('home/', views.HomePage,name= 'home'),
    path('problem/<int:problem_id>', views.problem_description,name= 'problem_description'),   
    path('problem/<int:problem_id>/verdict', views.submit_code,name="verdict"),
]
