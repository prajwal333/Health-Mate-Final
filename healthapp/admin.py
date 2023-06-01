from django.contrib import admin

# Register your models here.
from .models import doctor,consultationform
admin.site.register(doctor)
admin.site.register(consultationform)
