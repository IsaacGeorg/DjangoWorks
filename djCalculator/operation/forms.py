from django import forms

class RegistrationForm(forms.Form):

    email=forms.EmailField()
    username=forms.CharField()
    password1=forms.CharField()
    password2=forms.CharField()
    age=forms.IntegerField()


class VehicleForm(forms.Form):

    Name=forms.CharField()
    Running_km=forms.FloatField()

    rolechoice=(
        ("first","first"),
        ("second","second"),
        ("other","other")
    )

    Owner_type=forms.ChoiceField(choices=rolechoice)
    Price=forms.FloatField()

    fuel_choice=(
        ("petrol","petrol"),
        ("diesel","diesel"),
        ("CNG","CNG"),
        ("EV","EV"),
        ("hybrid","hybrid")
    )
    Fueltype=forms.ChoiceField(choices=fuel_choice)


# Calorie Calculation
class BmrForm(forms.Form):

    Weight=forms.FloatField()
    height=forms.FloatField()
    age=forms.IntegerField()

    gender_choice=(
        ("male","male"),
        ("female","female"),
        ("other","other")
    )
    gender=forms.ChoiceField(choices=gender_choice)

    activity_choice=(
        ("Sedantary","Sedantary"),
        ("Lightly Active","Lightly_Active"),
        ("Moderately Active","Moderately Active"),
        ("Very Active","Very Active"),
        ("Extra Active","Extra Active")
    )
    Activity_Level=forms.ChoiceField(choices=activity_choice)
    

class BmiForm(forms.Form):
    weight=forms.FloatField()
    height=forms.FloatField()

    
# class MilageForm(forms.Form):
#     distance=forms.FloatField()
#     consumption=forms.FloatField()


class BmrCalorieForm(forms.Form):

    weight=forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    height=forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    GENDER_CHOICE=(
        ("male","MALE"),
        ("female","FEMALE")
    )

    gender=forms.ChoiceField(choices=GENDER_CHOICE,widget=forms.Select(attrs={"class":"form-control mb-3 form-select"}))

    ACTIVITY_CHOICE=(
        (1.2,"SEDENTARY"),
        (1.375,"LIGHTLY ACTIVE"),
        (1.55,"MODERATELY ACTIVE"),
        (1.725,"VERY ACTIVE"),
        (1.9,"EXTRA ACTIVE")
    )

    activity=forms.ChoiceField(choices=ACTIVITY_CHOICE,widget=forms.Select(attrs={"class":"form-control mb-3 form-select"}))

