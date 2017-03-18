from django.contrib import admin

# Register your models here.
from StudlyApp.models import SchoolClasses

class SchoolClassesAdmin(admin.ModelAdmin):
    model = SchoolClasses
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(SchoolClasses, SchoolClassesAdmin)