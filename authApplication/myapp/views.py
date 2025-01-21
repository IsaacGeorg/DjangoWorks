from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.forms import SignUpForm, SignInForm
from myapp.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate,login
from django.core.mail import send_mail

# Create your views here.

def send_otp(user_instance):
    user_instance.generate_otp()

    send_mail(
        "django-app otp",
        user_instance.otp,
        "isacpman@gmail.com",
        [user_instance.email],
        fail_silently=False
    )


class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form_instance=SignUpForm()
        return render(request,"register.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        form_data=request.POST

        form_instance=SignUpForm(form_data)

        if form_instance.is_valid():
            user_instance=form_instance.save(commit=False)

            user_instance.is_active=False

            user_instance.save()
            
            send_otp(user_instance)

            return redirect("verify-otp")
        else:
            return render(request,"register.html",{"form":form_instance})


class VerifyOtpView(View):

    def get(self,request,*args,**kwargs):
        return render(request,"verifyotp.html")
    
    def post(self,request,*args,**kwargs):
        form_data=request.POST

        otp=form_data.get("otp")
        try:

            user_instance=User.objects.get(otp=otp)

            user_instance.is_active=True

            user_instance.is_verified=True

            user_instance.otp=None

            user_instance.save()

            return redirect("signin")
        
        except:
            
            messages.error(request,"Invalid OTP")
            return redirect("verify-otp")


class SignInView(View):
    def get(self,request,*args,**kwargs):
        form_instance=SignInForm()
        return render(request,"signin.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=SignInForm(form_data)

        if form_instance.is_valid():
            data=form_instance.cleaned_data

            uname=data.get("username")
            pwd=data.get("password")

            user_instance=authenticate(request,username=uname,password=pwd)

            if user_instance:
                login(request,user_instance)

        return render(request,"signin.html",{"form":form_instance})