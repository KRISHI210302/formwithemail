from django.shortcuts import render
from demo.form import CustomerDetails
from demo.models import Detail
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from django.core import mail


# Create your views here.
def form(request):
    det=CustomerDetails()
    context={
        'form':det
    }
    return render(request,'form.html',context)
def sub(request):
    data=Detail.objects.all()
    dic_data={"d":data}
    print(data)
    if  request.method=='POST':
        username=request.POST['username']
        number=request.POST['number']
        password=request.POST['password']
        re='kavya20020321@gmail.com'
        se= 'kavya20020321@gmail.com'
        print(username,number,password)
        data=Detail(username=username,number=number,password=password)
        data.save()
        email=EmailMessage(
            "test mail sub",
            'test mail body',
            settings.EMAIL_HOST_USER,
            [re]
        )
        email.send(fail_silently=False)
    return render(request,'index.html',context=dic_data)
"""def please(request):
    data=Detail.objects.all()
    context={
    "d":data
    }
    if  request.method=='POST':
        username=request.POST['username']
        number=request.POST['number']
        password=request.POST['password']
        print(username,number,password)
        data=Detail(username=username,number=number,password=password)
        data.save()
    return render(request,'index.html',context=context)"""