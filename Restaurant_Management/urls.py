"""Restaurant_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html')),
    path('base',views.base,name='base'),
    path('add_Restaurant', views.add_Restaurant, name='add_Restaurant'),
    path('insert_Restaurant', views.insert_Restaurant, name='insert_Restaurant'),
    path('view_Restaurant', views.view_Restaurant, name='view_Restaurant'),
    path('edit_Restaurant', views.edit_Restaurant, name='edit_Restaurant'),
    path('update_Restaurant', views.update_Restaurant, name='update_Restaurant'),
    path('delete_Restaurant', views.delete_Restaurant, name='delete_Restaurant'),
]
