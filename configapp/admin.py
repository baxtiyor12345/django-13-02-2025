
from django.contrib import admin
from .models import *

class KursAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_time', 'end_time', 'created_ed', 'updated_ed', 'is_bool')
    list_display_links = ['title']
    search_fields = ['title']

class StudentAdmin(admin.ModelAdmin):
    list_display=('id', 'full_name', 'phone_number', 'email', 'created_ed', 'updated_ed', 'is_bool')
    list_display_links = ['title']
    search_fields = ['full_name', 'kurs']


admin.site.register(Student)
admin.site.register(Kurs)

