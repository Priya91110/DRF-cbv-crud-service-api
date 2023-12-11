from django.contrib import admin
from .models import Course
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','price','duration','author','discount']
    
    
admin.site.register(Course, CourseAdmin)