from django.contrib import admin

# Register your models here.


from myapp.models import User

admin.site.register(User)