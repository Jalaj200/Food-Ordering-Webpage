from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.order_create, name='order_create'),
    path('payment/<int:order_id>/', views.payment_view, name='payment'),
    path('payment/verify/', views.payment_verify, name='payment_verify'),
    path('payment/success/<int:order_id>/', views.payment_success, name='success'),
    path('payment/failure/<int:order_id>/', views.payment_failure, name='failure'),
    path('track/<int:order_id>/', views.order_tracking, name='order_tracking'),
]
