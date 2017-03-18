from django.shortcuts import render, redirect

from StudlyApp.forms import CourseForm
from StudlyApp.models import Course


# Create your views here.
def index(request):
    courses = Course.objects.all()

    return render(request, 'index.html', {
        'courses': courses,
    })

def course_detail(request, slug):
    course = Course.objects.get(slug=slug)

    return render(request, 'Course/course_detail.html', {
        'course' : course,
    })

def edit_course(request, slug):
    course = Course.objects.get(slug=slug)

    form_class = CourseForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', slug=course.slug)
    else:
        form = form_class(instance=course)

    return render(request, 'Course/edit_course.html', {
        'course': course,
        'form' : form,
    })