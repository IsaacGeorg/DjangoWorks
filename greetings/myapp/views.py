from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class HelloWorldView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"Hello_World.html")
    

class GoodMorningView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"Good_Morning.html")
    

class GoodAfternoonView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"Good_Afternoon.html")
    

class GoodEveningView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"Good_Evening.html")

class SachinView(View):

    def get(self,request,*args,**kwargs):

        data={
            "age":52,
            "OD1":510,
            "tests":200,
            "centuries":100,
        }

        return render(request,"sachin.html",data)


class FeedbackView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'feedback.html')
    
    def post(self,request,*args,**kwargs):

        print("inside post method======")

        mail=request.POST.get('email')
        msg=request.POST.get('message')
        print(mail)
        print(msg)

        return render(request,'feedback.html')



class ReviewView(View):

    def get(self, request,*args,**kwargs):

        form_data=request.POST

        product=form_data.get('Product')
        comment=form_data.get('Comment')
        rating=form_data.get('Rating')

        print(product)
        print(comment)
        print(rating)

        return render(request,'review.html')