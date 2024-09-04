from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

from .models import Course, Evaluation

TokenAdmin.raw_id_fields = ['user']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'creation_date', 'update_date', 'isActive' )

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'email', 'comments', 'evaluation', 'creation_date', 'update_date', 'isActive')
