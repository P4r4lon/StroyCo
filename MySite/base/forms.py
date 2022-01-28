from django import forms

from .models import Deal, Apartment, Invoice, CounterAgent, Employer


class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ('contract', 'price', 'dateOfReg', 'employer', 'counteragent', 'invoice', 'apartment', 'dateOfCon',
                  'status_of_act')


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ('number', 'address', 'floor', 'square', 'price', 'status')


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('number', 'sum', 'dateOfPayment', 'dateOfIssue')


class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('name', 'position', 'address', 'phone', 'quantityOfDeals')


class CounterAgentForm(forms.ModelForm):
    class Meta:
        model = CounterAgent
        fields = ('name', 'phone', 'passport', 'address', 'date_of_birth')
