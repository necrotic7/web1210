from django.http import HttpResponse

def root(request):
    name=request.GET.get('name','guest')
    return HttpResponse('Hi,{}'.format(name))

def hello(request,name):
    return HttpResponse('hi,{}'.format(name))

def s(request,num):
    return HttpResponse(num**2)

def l(request,num1,num2):
    result=['<li>{}</li>'.format(i) for i in range(num1,num2+1)]
    return HttpResponse('<ul>{}</ul>'.format(''.join(result)))