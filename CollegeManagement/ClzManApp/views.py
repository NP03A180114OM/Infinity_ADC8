from django.shortcuts import render
from . models import Students
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def search(request):
    if request.method == "POST":
        search = request.POST['srh']

        if search:
            match = Students.objects.filter(StudentName__icontains = search)

            if match:
                return render(request, "search.html", {'sr':match})
    
            else:
                return HttpResponse("<H1>No Results Found</H1>")
        else:
            return HttpResponse("<H1>Type the Student Name<H1>")
    else:
        return render(request, "search.html")
        