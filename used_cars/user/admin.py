from django.contrib import admin
from .models import UserDetails, CarDetails,EnquiryDetails

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(CarDetails)
admin.site.register(EnquiryDetails)