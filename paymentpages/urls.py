from django.urls import path
from . import views
app_name = "paymentpages"
urlpatterns = [
    path('', views.initialize_payments, name="initialize_payment"),
    path('<str:reference>/', views.payments_verify, name="payments-verify"),
]