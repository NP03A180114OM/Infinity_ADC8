from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home.html',views.home, name='home'),
    path('students.html',views.students, name='students'),
    path('staff.html',views.staff, name='staff'),
    path('contact.html',views.contact, name='contact'),
    path('about.html',views.about, name='about'),
    path('search.html', views.search, name='search'),
    # path('upload/',views.upload),
    ]
# from django.urls import path
# from . import views
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('home.html', views.home, name='home'),
# ]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)