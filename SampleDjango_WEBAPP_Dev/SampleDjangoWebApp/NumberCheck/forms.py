from django import forms
class LargestForm(forms.Form):
    Number1=forms.IntegerField()
    Number2=forms.IntegerField()


class EvenOddForm(forms.Form):
    Number=forms.IntegerField()

class PrimeForm(forms.Form):
    Numb=forms.IntegerField()