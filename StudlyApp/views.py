from django.shortcuts import render
from StudlyApp.models import SchoolClasses

# Create your views here.
def index(request):
    classes = SchoolClasses.objects.all()

    return render(request, 'index.html', {
        'classes': classes,
    })

def class_detail(request, slug):
    schoolClass = SchoolClasses.objects.get(slug=slug)

    return render(request, 'schoolClasses/class_detail.html', {
        'schoolClass' : schoolClass,
    })