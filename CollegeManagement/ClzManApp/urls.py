from django.contrib import admin
from django.urls import path,include
from . views import *

urlpatterns = [
    #for staff
    path('studentdata/',view_student_lists),
    path('studentform/',view_student_form),
    path('studentform/save',view_studentdata_save),
   
    #for staff
    path('staffdata/',view_staff_lists),
    path('staffform/',view_staff_form),
    path('staffform/save',view_staffdata_save),
    path('staffdata/delete/<int:ID>',view_staff_delete), 
]
