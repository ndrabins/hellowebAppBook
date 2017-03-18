from django.contrib import admin

# Register your models here.
from StudlyApp.models import Course

class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Course, CourseAdmin)