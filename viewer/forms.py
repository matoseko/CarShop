from django import forms
from django.forms import ModelForm, CharField, DateField, FloatField, ModelChoiceField, ImageField, Textarea
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from viewer.models import Item, Transmission, Fuel, Brand

PAYMENT = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)

class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '1234 Main St'
    }))

    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Apartment or suite'
    }))

    country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={
        'class': 'custom-select d-block w-100'
    }))

    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    same_billing_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT)

class ItemModelForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    item_name = CharField(max_length=128)
    produced = DateField()
    price = FloatField()
    color = CharField(max_length=55)
    description = CharField(widget=Textarea)
    transmission = ModelChoiceField(queryset=Transmission.objects)
    fuel = ModelChoiceField(queryset=Fuel.objects)
    brand = ModelChoiceField(queryset=Brand.objects)
    image = ImageField()
    discount_price = FloatField()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


