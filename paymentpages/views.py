from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from . import forms
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Payments
from paystackapi.paystack import Paystack

# Create your views here.
def initialize_payments(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        payment_form = forms.PaymentsForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save(commit=False)
            payment.email = payment_form.cleaned_data['email']
            payment.amount = payment_form.cleaned_data['amount'] 
            payment.save()
            return render(request, 'paymentpages/payment.html', {'payment':payment, 'public_key': settings.PUBLIC_KEY})
    else:
        payment_form = forms.PaymentsForm()
    return render(request, 'paymentpages/create_payment.html', {'form': payment_form})

def payments_verify(request: HttpRequest, reference: str) -> HttpResponse:
    paystack = Paystack(secret_key=settings.PUBLIC_KEY)
    payment = paystack.transaction.verify(reference)
    if payment:
        messages.success(request, "Verification successful")
    else:
        messages.error(request, "Verifcation failed")
    return redirect('paymentpages:initialize_payment')

