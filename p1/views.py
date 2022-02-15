from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.mail import send_mail

def submit(request):
    var1=request.POST.get('email','none')
    var2=request.POST.get('ammount','none')
    print(var1,var2)
    dict={'var2':var2}

    send_mail('Donation', f' we have received your donated ammount of {var2}', 'sdsoumyadey2910@gmail.com', [var1],
              fail_silently=False)

    return render(request,'payment.html',dict)
def payment(request):

    return render(request, 'payment.html')
