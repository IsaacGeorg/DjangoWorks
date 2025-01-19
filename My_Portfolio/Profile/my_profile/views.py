from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import View

class MyProfileView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'portfolio.html')