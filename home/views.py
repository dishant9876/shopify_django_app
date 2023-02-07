from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.views import APIView, Response  
from rest_framework.decorators import api_view
import shopify
import requests
from django.views.generic import ListView, CreateView, UpdateView, View
from shopify_app.decorators import shop_login_required
from django.core.mail import send_mail
from django.conf import settings



@shop_login_required
def index(request):
    products = shopify.Product.find(limit=1)
    # orders = shopify.Order.find(limit=3, order="created_at DESC")
    return render(request, 'home/index.html', {'products': products, 'orders': []})

@api_view(['POST','GET'])
def customer_data_request(request):
    return Response({"message":"success"},status=200)

@api_view(['POST','GET'])
def customer_redact(request):
    return Response({"message":"success"},status=200)

@api_view(['POST','GET'])
def shop_redact(request):
    return Response({"message":"success"},status=200)

def contactus(request):
    url = "https://farzipromo-stage.farziengineer.co/shopify/success"
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.json())
    print(response.status_code)
    print(response.text)
    # orders = shopify.Order.find(limit=3, order="created_at DESC")
    return render(request, 'home/contact-us.html', {'orders': []})

class ContactUsView(View):
    def get(self, request):
        return render(request, 'home/contact-us.html')
    def post(self, request):
        # print(request.POST.get('email_id'))
        sendmail_contactus_sendgrid(request.POST.get('email_id'),request.POST.get('shop_url'),request.POST.get('mob_no'),request.POST.get('message'))
        return render(request, 'home/contact-us.html')


def sendmail_contactus_sendgrid(email_address, shop_url, mobile_no, message):
    your_message = f"Email address: {email_address}\n Shop URL: {shop_url}\n Mobile Number: {mobile_no}\n Message: {message}"
    send_mail('FarziPromo Integration Shopify', your_message, settings.DEFAULT_FROM_EMAIL, ['dishant.w@farziengineer.com'])

