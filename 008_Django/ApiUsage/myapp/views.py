from django.shortcuts import render,HttpResponse
import requests
import random
from django.core.mail import send_mail
from django.conf import settings
import razorpay
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,"index.html")

def otp(request):
    return render(request,"otp.html")

def sendsms(request):
    if request.method=="POST":
        phone = request.POST['phone']
    number = random.randint(100,999)
    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {"authorization":"","variables_values":number,"route":"otp","numbers":phone}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    
    return HttpResponse(response.text)


def send_mail_page(request):
    context = {}

    # if request.method == 'POST':
    #     address = request.POST.get('address')
    #     subject = request.POST.get('subject')
    #     message = request.POST.get('message')
    address = "chintan.tops@gmail.com"
    subject = "Test"
    message = "Testing..."
    
    if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
    else:
            context['result'] = 'All fields are required'
    
    return HttpResponse(context)

def payment(request):
     return render(request,"payment.html")

def makepayment(request):
    amt = request.GET['amt']
   
    
    client = razorpay.Client(auth=("rzp_test_pv6FbtEGoD0n4P", "iladq0iIJ4h3mt2LyxAalTuK"))

    data = { "amount": int(amt)*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) 
    return JsonResponse(payment)