from django.contrib import admin
from .models import deptmodel,doctorsmodel,bookingmodel,signupmodel

# Register your models here.
class deptadmin(admin.ModelAdmin):
    list_display=('dep_name','dep_desc')
admin.site.register(deptmodel,deptadmin)
class doctorsadmin(admin.ModelAdmin):
    list_display=('doc_name','doc_spec','dep_name','doc_image')
admin.site.register(doctorsmodel,doctorsadmin)
class bookingadmin(admin.ModelAdmin):
    list_display=('p_name','p_phone','p_email','doc_name','booking_date')
admin.site.register(bookingmodel,bookingadmin)
admin.site.register(signupmodel)