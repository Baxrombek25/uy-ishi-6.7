from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'gpa')
    list_filter = ('gpa',)
    search_fields = ('name',)