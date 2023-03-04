from django import forms

from .models import Payments

class PaymentsForm(forms.ModelForm):
    email = forms.EmailField(label='Email', help_text='Required', widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Email',
        'id': 'form-email'}))
    amount = forms.FloatField(label='Amount', help_text='Required', widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Amount',
        'id': 'form-amount'}))
    
    class Meta:
        model = Payments
        fields = ("email", "amount",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].error_messages = {
            'required': 'Sorry!, you need an email address',
            'invalid': 'Please enter a valid email address',
        }
        self.fields['amount'].error_messages = {
            'required': 'Amount required',
            'invalid': 'Please enter a valid amount',
        }