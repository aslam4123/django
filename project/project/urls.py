"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls'))
    # path('func',views.func),
    # path('fun1/<a>',views.fun1),
    # path('task/<int:salary>/<int:year>',views.task),
    # path('task1/<city>',views.task1),
    # path('task2/<int:num>',views.task2),
    # path('task3/<int:day>',views.task3),
    # path('task4/<int:cost>',views.task4),
    # path('task5/<int:unit>',views.task5),


]
