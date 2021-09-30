
from django.contrib import admin
from django.urls import path
from django.urls.conf import include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/', include('django.contrib.auth.urls')),  
    # "common/"  folder need to path need to add  here otherwise html file of common will not redirect to templet 
    #this url is for forrget password's href href="{% url 'password_reset' %}" 
    #if will not add path below 1st path i.e(path('admin/', admin.site.urls)) then  it will not redirect to template file
    # after that
    path('', include('userApp.urls')),


] 
