from django.contrib import admin

from .models import Course, Evaluation

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'creation_date', 'update_date', 'isActive' )

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'email', 'comments', 'evaluation', 'creation_date', 'update_date', 'isActive')
