from django.shortcuts import render
from StudlyApp.models import SchoolClasses

# Create your views here.
def index(request):
    classes = SchoolClasses.objects.all()

    return render(request, 'index.html', {
        'classes': classes,
    })