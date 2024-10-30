from django.urls import path
from . import views
urlpatterns=[
    path('task/<int:salary>/<int:year>',views.task),
    path('task1/<city>',views.task1),
    path('task2/<int:num>',views.task2),
    path('task3/<int:day>',views.task3),
    path('task4/<int:cost>',views.task4),
    path('task5/<int:unit>',views.task5),
    path('demo',views.demo),
    path('display',views.display),
    path('user_reg',views.user_reg),
    path('edit_user/<id>',views.edit_user),
    path('delete_user/<id>',views.delete_user),
    path('',views.index),
    path('dis_std',views.display_std),
    path('add_std',views.add_std),
    path('edit_std/<id>',views.edit_std),
    path('delete_std/<id>',views.delete_std),


]