from django.forms import ModelForm

from StudlyApp.models import Course

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'description',)