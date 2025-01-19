from django.shortcuts import render
from django.views.generic import View
# Create your views here.

from NumberCheck.forms import LargestForm

class NumCheckView(View):
    def get(self,request,*args,**kwargs):
        form_instance=LargestForm()
        return render(request,'numcheck.html',{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        form_data=request.POST

        form_instance=LargestForm(form_data)

        if form_instance.is_valid():
            data=form_instance.cleaned_data

            num1=data.get("Number1")
            num2=data.get("Number2")
            
            if num1>num2:
                result=num1
            else:
                result=num2


            return render(request,'numcheck.html',{"result1":result})
            

from NumberCheck.forms import EvenOddForm
class EvenOddView(View):
    def get(self,request,*args,**kwargs):
        form_instant=EvenOddForm()
        return render(request,'numcheck.html',{"form2":form_instant})
    
    def post(self,request,*args,**kwargs):
        form_data=request.POST

        form_instant=EvenOddForm(form_data)

        if form_instant.is_valid():
            data=form_instant.cleaned_data

            number=data.get("Number")
            

            if number%2==0:
                res=number,"is Odd Number."
            else:
                res=number,"is an Even Number."

            return render(request,'numcheck.html',{"result2":res})
            


from NumberCheck.forms import PrimeForm
class PrimeView(View):
    def get(self,request,*args,**kwargs):
        form_instance=PrimeForm()
        return render(request,'numcheck.html',{"form3":form_instance})
    
    def post(self,request,*args,**kwargs):
        form_data=request.POST

        form_instance=PrimeForm(form_data)

        if form_instance.is_valid():
            data=form_instance.cleaned_data

            numb=data.get("Numb")
            
            for i in range(2,numb-1):
                if numb%i==0:
                    res=numb,"is Prime Number."
                else:
                    res=numb,"is a Composite Number."

            return render(request,'numcheck.html',{"result3":res})
            
