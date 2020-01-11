# from django.urls import path
# from . import views
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('home.html', views.home, name='home'),
# ]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


from django.urls import path
from .views import *

urlpatterns=[
    path('upload/',upload)
]