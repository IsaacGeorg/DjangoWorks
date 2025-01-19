"""
URL configuration for djCalculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from operation.views import AdditionView
from operation.views import SubtractionView
from operation import views

from operation import views
from operation.views import BmrView

from operation.views import BmiView

from operation.views import BmrCalorieView
from operation.views import IndexView
urlpatterns = [
    path('admin/', admin.site.urls),

    path('addition/',AdditionView.as_view(),name='add'),

    path('sub/',SubtractionView.as_view()),

    path('register-form/',views.SignUpView.as_view(),name='register'),

    path('vehicle-form/',views.VehicleFormView.as_view(),name="vehicle"),

    path('bmrCalculation/',BmrView.as_view()),

    path('bmi/',BmiView.as_view()),

    path('calorie/',BmrCalorieView.as_view(),name="calorie"),

    path("",IndexView.as_view(),name="index")
]
