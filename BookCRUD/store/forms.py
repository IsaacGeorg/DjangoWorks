from django import forms

# class BookForm(forms.Form):
#     title=forms.CharField()
#     author=forms.CharField()
#     price=forms.IntegerField()
#     language=forms.CharField()
#     genre=forms.CharField()
#     year=forms.IntegerField()
#     image=forms.ImageField()

# from store.models import forms
from store.models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model=Book
        fields="__all__"

        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "language":forms.TextInput(attrs={"class":"form-control"}),
            "genre":forms.TextInput(attrs={"class":"form-control"}),
            "year":forms.NumberInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
        }