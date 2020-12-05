from django.contrib import admin
from .models import *
# Register your models here.

def read(modeladmin, request, queryset):
    queryset.update(read=True)
read.short_description= 'Update the Selected message(s) to Read'

class ContactUsAdmin(admin.ModelAdmin):
    list_display= [
        'name',
        'email',
        'phoneNo',
        'message',
        'read'
    ]

    list_filter= [ 
        'name',
        'email',
        'phoneNo',
        'read'
    ]

    search_fields= [
        'name',
        'email',
        'phoneNo',
    ]

    actions=[read]

admin.site.register(AboutUs)
admin.site.register(ContactUs, ContactUsAdmin)