from dataclasses import field
from django import forms
from .models import *



class ContactForm(forms.ModelForm):
    services={
        ('----','-----'),
        ('Brand Guideline','Brand Guideline'),
        ('Brand Audit','Brand Audit'),
        ('Brand Stories','Brand Stories'),
        ('Brand Design','Brand Design'),
        ('Direct Mail Services Design','Direct Mail Services Design'),
        ('Corporate Identity','Corporate Identity'),
        ('Merchandising Services Design','Merchandising Services Design'),
        ('Product Concept & Design','Product Concept & Design'),
        ('Stall Design & Mall Activity','Stall Design & Mall Activity'),
        ('Signage & Display Design','Signage & Display Design'),
        ('3D Advertising Video','3D Advertising Video'),
        ('Market Research','Market Research')
        

    }
    service =forms.ChoiceField(  required=False ,initial='----',choices=services ,widget=forms.Select(attrs={'class': 'form-control'}))

    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeHolder':"Enter Email"}))
    number = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeHolder':"Number"}))
    fname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeHolder':"Enter First Name"}))
    comment=forms.CharField(required=False ,widget=forms.Textarea(attrs={'class':'form-control','placeHolder':"Tell us more about your project, needs, and timeline."}))
    website=forms.CharField(required=False ,widget=forms.TextInput(attrs={'class':'form-control','placeHolder':"Business Name Or URL"}))

    class Meta:
        model= Contact
        exclude=['date']
  
