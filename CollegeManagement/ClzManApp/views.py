from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import Context

# Create your views here.

def addData(request):
    return render(request,"add_data.html")

#this method is for add student
def add_student(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Now Allowed</h2>")
    else:
        file=request.FILES['profile']
        fs=FileSystemStorage()
        profile_img=fs.save(file.name,file)
        try:
            course=Courses.objects.get(id=request.POST.get('course',''))
            student=Students(name=request.POST.get('name',''),email=request.POST.get('email',''),standard=request.POST.get('standard',''),hobbies=request.POST.get('hobbies',''),roll_no=request.POST.get('roll_no',''),bio=request.POST.get('bio',''),profile_image=profile_img,course=course)
            student.save()


            subject_list=request.POST.getlist('subjects[]')
            for subject in subject_list:
                subj=Subjects.objects.get(id=subject)
                student_subject=StudentSubjects(subject_id=subj,student_id=student)
                student_subject.save()
            messages.success(request,"Added Successfully")
        except Exception as e:
            print(e)
            messages.error(request,"Failed to Add Student")

        return HttpResponseRedirect("/addData")


#this method is for add teacher
def add_teacher(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Now Allowed</h2>")
    else:
        try:
            teacher=Teachers(name=request.POST.get('name',''),email=request.POST.get('email',''),department=request.POST.get('department',''))
            teacher.save()
            messages.success(request,"Added Successfully")
        except:
            messages.error(request,"Failed to Add Teacher")

        return HttpResponseRedirect("/addData")





