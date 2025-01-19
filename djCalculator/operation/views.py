from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class AdditionView(View):
    
    def get(self, request,*args,**kwargs):

        return render(request,'add.html')
    
    def post(self,request,*args,**kwargs):

        a=request.POST.get("num1")
        b=request.POST.get("num2")
        result=int(a)+int(b)
        data={"output":result}
        return render(request,'add.html',data)
    
class SubtractionView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'add.html')
    
    def post(self,request,*args,**kwargs):

        n1=request.POST.get('n1')
        n2=request.POST.get('n2')

        result=int(n1)-int(n2)

        data={"out":result}

        return render(request,'add.html',data)


# Registration form 

from operation.forms import RegistrationForm
class SignUpView(View):

    def get(self,request,*args,**kwargs):

        form_instance=RegistrationForm()

        context={"form":form_instance}

        return render(request,'register.html',context)
    

from operation import forms
class VehicleFormView(View):

    def get(self,request,*args,**kwargs):

        form_instance=forms.VehicleForm()

        context={"form":form_instance}

        return render(request,'vehicle.html',context)
    

from operation import forms
class BmrView(View):
    def get(self,request,*args,**kwargs):

        bmr_instance=forms.BmrForm()

        context={"bmr_form":bmr_instance}

        return render(request,"bmr.html",context)
    
from operation.forms import BmiForm
class BmiView(View):
    def get(self,request,*args,**kwargs):

        bmi_instance=BmiForm()

        return render(request,'bmi.html',{"form":bmi_instance})
    

    def post(self,request,*args,**kwargs):

        # extract form data
        form_data=request.POST

        # initialize form instance with form_data
        form_instance=BmiForm(form_data)

        # validating cleaned data
        if form_instance.is_valid():

            data = form_instance.cleaned_data

            height=data.get('height')
            weight=data.get('weight')
            BMI=weight/(height/100)**2
            print(BMI)

        return render(request,'bmi.html',{"form":form_instance,"result":BMI})
    
# from operation import forms
# class MilageView(View):

#     def get(self,request,*args,**kwargs):

#         milage_instance=forms.MilageForm()

#         return render(request,'milage.html',{"form":milage_instance})
    
    
from operation.forms import BmrCalorieForm
class BmrCalorieView(View):

    def get(self,request,*args,**kwargs):

        form_instance=BmrCalorieForm()
        context={
            "form":form_instance
        }
        return render(request,"calorie.html",context)
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=BmrCalorieForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data
            print(data)

            weight=data.get("weight")
            height=data.get("height")
            age=data.get("age")
            gender=data.get("gender")
            if gender=="male":
                bmr=10*weight + 6.25*height -5*age +5
                
            else:
                bmr=10*weight + 6.25*height -5*age -161
            
            activity=data.get("activity")

            result=bmr
            calorie=result*float(activity)


            # 10*wei + 6.25*hei -5*age +5
            # 10*wei + 6.25*hei -5*age -161

        return render(request,'calorie.html',{"form":form_instance,"result":bmr,"calorie":calorie})
    


class IndexView(View):
    def get(self,request,*args,**kwargs):

        return render(request,'index.html')