from django.shortcuts import render
from django.http import HttpResponse
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