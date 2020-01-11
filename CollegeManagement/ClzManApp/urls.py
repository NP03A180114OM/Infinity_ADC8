from django.contrib import admin
from django.urls import path,include
from . views import *

urlpatterns = [
    #for staff
    path('studentdata/',view_student_lists),
    path('studentform/',view_student_form),
    path('studentform/save',view_studentdata_save),
    path('studentdata/edit/<int:ID>',view_studentdata_updateform),
    path('studentdata/edit/update/<int:ID>',view_update_form_data_in_db),
    #for staff
    path('staffdata/',view_staff_lists),
    path('staffform/',view_staff_form),
    path('staffform/save',view_staffdata_save),
    path('staffdata/edit/<int:ID>',view_staffdata_updateform),
    path('staffdata/edit/update/<int:ID>',view_update_form_data_in_db),
    #path('delete_staffdata/<str:TeacherID>',view_delete_staff,name="delete_Teacher"),
    path('staffdata/delete/<int:ID>',view_staff_delete), 
]