from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from SignApp.forms import SignUpForm


class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form_instance=SignUpForm()
        return render(request,'Signup.html',{"form":form_instance})