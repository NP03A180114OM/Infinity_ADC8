
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
# Create your views here.
def home(request):
     return render(request, 'home.html')
def students(request):
     return render(request, 'students.html')
def staff(request):
     return render(request, 'staff.html')
def contact(request):
     return render(request, 'contact.html')
def about(request):
     return render(request, 'about.html')
def search(request):
     return render(request,'search.html')


# Create your views here.


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['doc']
        file_object = FileSystemStorage()
        file_object.save(uploaded_file.name, uploaded_file)
    return render(request,'home.html')
