from django.shortcuts import render,HttpResponse
import requests
import random
from django.core.mail import send_mail
from django.conf import settings

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

    querystring = {"authorization":"WXfAe5cjnlMG0thTkdLD9IsgRyZbS7w41UzP3H8mKiqQNVEova9vDJtywEXpMNoUieOfPlq1r8HhdnTL","variables_values":number,"route":"otp","numbers":phone}

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