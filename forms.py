from dataclasses import fields
from django.core import validators
from django import forms
# from matplotlib import widgets
from accounts.models import Customers

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields=['customerid','name','Account_no','Branch','IFSC','phone','Address']
        widgets={
            'customerid':forms.NumberInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'Account_no':forms.NumberInput(attrs={'class':'form-control'}),
            'Branch':forms.TextInput(attrs={'class':'form-control'}),
            'IFSC':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),

        }
    





        # fields = '__all__'
