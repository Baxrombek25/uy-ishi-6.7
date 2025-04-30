from django.shortcuts import render, get_object_or_404
from .models import Student

def student_list(request):
    students = Student.objects.filter(gpa__gt=3.0)
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'students/student_detail.html', {'student': student})