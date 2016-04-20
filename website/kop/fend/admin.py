from django.contrib import admin
from .models import Mydata, UserProfile, ContactInfo, MyDataQuery

# Register your models here.
admin.site.register(Mydata)
admin.site.register(UserProfile)
admin.site.register(ContactInfo)
admin.site.register(MyDataQuery)