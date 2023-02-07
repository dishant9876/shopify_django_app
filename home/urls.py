from django.urls import path
from .views import *
# from . import views  

urlpatterns = [
    path('', index, name='root_path'),
    path('customers/data_request', customer_data_request, name='customer_data_request'),
    path('customers/redact', customer_redact, name='customer_redact'),
    path('shop/redact', shop_redact, name='shop_redact'),
    path('contact-us', ContactUsView.as_view(), name='contact-us')
]
