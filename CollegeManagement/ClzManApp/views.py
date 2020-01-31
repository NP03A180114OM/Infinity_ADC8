
from django.shortcuts import render

# Create your views here.


def index(request):
    from .models import User
    users = User.objects.all()
    p = users[len(users)-1].pic
    print(p.url)
    return render(request, 'index.html' , {'users': users})



def uploadImage(request):
    print("Request Handling...")
    p = request.FILES['image']
    from .models import User

    user = User(pic =p)
    user.save()
    return render(request, 'index.html')
