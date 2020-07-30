from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PAyPal'),
)


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '1234 Main St',
        'id': 'street_address'
    }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Apartment or Suite'
    }))
    country = CountryField(blank_label='(select country)').formfield(
        widget=CountrySelectWidget(
            attrs={
                'class': 'custom-select d-block w-100',
            }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    same_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class SendMailForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your name',
        'id': 'first_name'
    }))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your last-name',
        'id': 'last_name'
    }))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder': 'Example: +380671234567',
        'id': 'phone'
    }))
    comment = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={
        'placeholder': 'Briefly describe tour question...'
    }))


