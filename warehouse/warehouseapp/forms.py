from django import forms
from .models import Customers

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['username', 'first_name', 'last_name', 'street', 'street_number', 'email', 'postal_code', 'city']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        street = cleaned_data.get('street')
        street_number = cleaned_data.get('street_number')
        postal_code = cleaned_data.get('postal_code')
        city = cleaned_data.get('city')

        # Check if a customer with similar information already exists
        if Customers.objects.filter(username=username, first_name=first_name, last_name=last_name, email=email, street=street, street_number=street_number, postal_code=postal_code, city=city).exists():
            raise forms.ValidationError("A customer with these details already exists.")