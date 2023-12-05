from django import forms
from .models import Property, Unit, Tenant, RentalInformation



class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'address', 'location', 'features']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'features': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['rent_cost', 'unit_type']
        widgets = {
            'rent_cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_type':  forms.Select(attrs={'class': 'form-control'}),
        }

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'address', 'document_proof']

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'address': forms.Textarea(attrs={'class': 'form-control'}),
        'document_proof': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }


class RentalInformationForm(forms.ModelForm):
    class Meta:
        model = RentalInformation
        fields = ['tenant', 'agreement_end_date', 'monthly_rent_date']
        #'unit'

        widgets = {
            'tenant': forms.Select(attrs={'class': 'form-control'}),
            #'unit': forms.Select(attrs={'class': 'form-control'}),
            'agreement_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'monthly_rent_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }