from django import forms

class SignUpForm(forms.Form):
    Username=forms.CharField()
    Email=forms.CharField()
    Password=forms.CharField()