from django.urls import path
from . import views
urlpatterns=[
    path('',views.drs_login),
    path('home',views.home),
    path('drs_logout',views.drs_logout),
    path('add_prod',views.add_prod),
    path('edit/<pid>',views.edit),
    path('delete/<pid>',views.delete)

]