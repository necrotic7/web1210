from django.http import HttpResponse
from django.shortcuts import render

def root(request):
    name=request.GET.get('name','guest')
    return HttpResponse('Hi,{}'.format(name))

def hello(request,name):
    return HttpResponse('hi,{}'.format(name))

def s(request,num):
    return HttpResponse(num**2)

def l(request,num1,num2):
    
    step = -1 if num1 > num2 else 1
    result=range(num1,num2+step,step)

    # if num1<num2:
    #     result=range(num1,num2+1)
    # else :
    #     result=reversed(range(num2,num1+1))

    return render(request,'l.html',{'list':result})