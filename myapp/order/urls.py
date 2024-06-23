from django.urls import path
from . import views

app_name='order'

urlpatterns = [
    path('create/', views.order_create , name = 'order_create'),
    path('invoice/<int:order_id>/', views.order_invoice, name='invoice'),
    
]