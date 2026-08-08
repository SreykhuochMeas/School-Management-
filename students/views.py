from datetime import date
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CourseForm, StudentForm
from .models import Course, Student

# --- Student Views ---

def student_list_view(request):
    students = Student.objects.all().order_by('id')
    
    query = request.GET.get('q', '')
    status = request.GET.get('status', '')
    result = request.GET.get('result', '')

    if query:
        students = students.filter(Q(name__icontains=query) | Q(email__icontains=query))

    if status == 'active':
        students = students.filter(is_active=True)
    elif status == 'inactive':
        students = students.filter(is_active=False)

    if result == 'pass':
        students = students.filter(score__gte=50)
    elif result == 'fail':
        students = students.filter(score__lt=50)

    total_filtered_students = students.count()

    paginator = Paginator(students, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'students': page_obj,
        'page_obj': page_obj,
        'total_students': total_filtered_students,
        'today': date.today(),
        'query': query,
        'status': status,
        'result': result,
    }
    return render(request, 'students/student_list.html', context)

def active_student_list_view(request):
    students = Student.objects.filter(is_active=True).order_by('id')
    context = {
        'students': students,
        'total_students': students.count(),
        'today': date.today(),
    }
    return render(request, 'students/student_list.html', context)

def home_view(request):
    return render(request, 'students/home.html', {'today': date.today()})

def about_view(request):
    return render(request, 'students/about.html')

def contact_view(request):
    return render(request, 'students/contact.html')

def student_detail_view(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/student_detail.html', {'student': student})

def student_name_view(request, name):
    students = Student.objects.filter(name__icontains=name).order_by('id')
    context = {
        'students': students, 
        'total_students': students.count(),
        'today': date.today()
    }
    return render(request, 'students/student_list.html', context)

def student_create_view(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Student created successfully.")
        return redirect('student_list')
    context = {
        'form': form, 
        'action': 'Create',
        'today': date.today()
    }
    return render(request, 'students/student_form.html', context)

def student_update_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        messages.success(request, "Student updated successfully.")
        return redirect('student_list')
    context = {
        'form': form, 
        'action': 'Update',
        'today': date.today()
    }
    return render(request, 'students/student_form.html', context)

def student_delete_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "Student deleted successfully.")
        return redirect('student_list')
    context = {
        'student': student,
        'today': date.today()
    }
    return render(request, 'students/student_confirm_delete.html', context)


# --- Course Views ---

def course_list_view(request):
    courses = Course.objects.all().order_by('id')
    context = {
        'courses': courses,
        'total_courses': courses.count(),
        'today': date.today()
    }
    return render(request, 'students/course_list.html', context)

def course_detail_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    context = {
        'course': course,
        'today': date.today()
    }
    return render(request, 'students/course_detail.html', context)

def course_create_view(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Course created successfully.")
        return redirect('course_list')
    context = {
        'form': form, 
        'action': 'Create',
        'today': date.today()
    }
    return render(request, 'students/course_form.html', context)

def course_update_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        messages.success(request, "Course updated successfully.")
        return redirect('course_list')
    context = {
        'form': form, 
        'action': 'Update',
        'today': date.today()
    }
    return render(request, 'students/course_form.html', context)

def course_delete_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        messages.success(request, "Course deleted successfully.")
        return redirect('course_list')
    context = {
        'course': course,
        'today': date.today()
    }
    return render(request, 'students/course_confirm_delete.html', context)