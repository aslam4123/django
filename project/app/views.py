from django.shortcuts import render
from django.http import HttpResponse
def func(req):
    a=[12,34]
    return HttpResponse(a)
def fun1(req,a):
    return HttpResponse(a)
def task(req,salary,year):
    if year>5:
        bonus=(salary/100*5)
        return HttpResponse(bonus)
    else:
        return HttpResponse('year of service lessthan 5')
def task1(req,city):
    if city=='Delhi':
        return HttpResponse('Red fort')
    elif city=='Agra':
        return HttpResponse('Taj mahal')
    elif city=='Jaipur':
        return HttpResponse('Jal mahal')
    else:
        return HttpResponse('invalid input')
def task2(req,num):
    n=num%10
    if n%3==0:
        return HttpResponse('divisible by 3')
    else:
        return HttpResponse('not divisible by 3')

        # Create your views here.
