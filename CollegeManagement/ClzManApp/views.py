from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template,Context
from .models import Students
from .models import Teachers

# Create your views here.
#this views for student
def view_students_page(request):
    return render(request,'student/student.html')

def view_student_lists(request):
    list_of_students= Students.objects.all()
    print(list_of_students)
    context_variable = {
        'students':list_of_students
    }
    return render(request,'student/student.html',context_variable)

def view_student_form(request):
    return render(request,'student/studform.html')

def view_studentdata_save(request):
    if request.method == "POST":
        get_all = request.POST
        get_StudentID = request.POST['student_StudentID']
        print(type(get_StudentID))
        get_StudentName = request.POST['student_StudentName']
        get_email = request.POST['student_email']
        print(get_StudentID)
        get_standard = request.POST['student_standard']
        print(type(get_StudentID))
        student_obj = Students(StudentID=get_StudentID,StudentName=get_StudentName,email=get_email,standard=get_standard)
        student_obj.save()
        return HttpResponse("Record Saved")
    else:
        return HttpResponse("Error record saving")


#this views for staff
def view_staffs_page(request):
    return render(request,'staff/staff.html')

def view_staff_lists(request):
    list_of_staff= Teachers.objects.all()
    print(list_of_staff)
    context_variable = {
        'staff':list_of_staff
    }
    return render(request,'staff/staff.html',context_variable)

def view_staff_form(request):
    return render(request,'staff/staffform.html')

def view_staffdata_save(request):
    if request.method == "POST":
        get_all = request.POST
        get_TeacherID = request.POST['staff_TeacherID']
        print(type(get_TeacherID))
        get_TeacherName = request.POST['staff_TeacherName']
        get_email = request.POST['staff_email']
        print(get_TeacherID)
        get_department = request.POST['staff_department']
        print(type(get_TeacherID))
        staff_obj = Teachers(TeacherID=get_TeacherID,TeacherName=get_TeacherName,email=get_email,department=get_department)
        staff_obj.save()
        return HttpResponse("Record Saved")
    else:
        return HttpResponse("Error record saving")
    

def view_staff_delete(request,ID):  
    print(ID)
    staff_obj = Teachers.objects.get(id=ID)  
    context_variable={
        'staff':staff_obj
    }
    staff_obj.delete()
    return render(request,'staff/staffdelete.html',context_variable) 
