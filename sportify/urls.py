"""sportify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from sponsor.views import *
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('register/',register,name='register'),
    path('',include("django.contrib.auth.urls")),
    path('athletes',athletes,name='athletes'),
    path('sponsors',sponsors,name='sponsors'),
    path('addAthlete/',addAthlete,name="addAthlete"),
    path('addSponsor/',addSponsor,name="addSponsor"),
    path('delete_athlete/<str:id>/',athleteDelete,name='athleteDelete'),
    path('update_athlete/<str:id>/',athleteUpdate,name='athleteUpdate'),
    path('delete_sponsor/<str:id>/',sponsorDelete,name='sponsorDelete'),
    path('update_sponsor/<str:id>/',sponsorUpdate,name='sponsorUpdate'),



]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  

