from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.db.utils import OperationalError
from .models import Student, College, Program, Organization

def dashboard(request):
    try:
        context = {
            'students_count': Student.objects.count(),
            'colleges_count': College.objects.count(),
            'programs_count': Program.objects.count(),
            'organizations_count': Organization.objects.count(),
        }
    except OperationalError:
        context = {
            'students_count': 0,
            'colleges_count': 0,
            'programs_count': 0,
            'organizations_count': 0,
        }
    return render(request, 'core/dashboard.html', context)

class StudentListView(ListView):
    model = Student
    template_name = 'core/student_list.html'
    context_object_name = 'students'

class CollegeListView(ListView):
    model = College
    template_name = 'core/college_list.html'
    context_object_name = 'colleges'

class ProgramListView(ListView):
    model = Program
    template_name = 'core/program_list.html'
    context_object_name = 'programs'

class OrganizationListView(ListView):
    model = Organization
    template_name = 'core/organization_list.html'
    context_object_name = 'organizations'

# Create Views
class StudentCreateView(CreateView):
    model = Student
    template_name = 'core/student_form.html'
    fields = ['first_name', 'last_name', 'student_id', 'program']
    success_url = reverse_lazy('student_list')

class CollegeCreateView(CreateView):
    model = College
    template_name = 'core/college_form.html'
    fields = ['name', 'code', 'description']
    success_url = reverse_lazy('college_list')

class ProgramCreateView(CreateView):
    model = Program
    template_name = 'core/program_form.html'
    fields = ['name', 'code', 'description', 'college']
    success_url = reverse_lazy('program_list')

class OrganizationCreateView(CreateView):
    model = Organization
    template_name = 'core/organization_form.html'
    fields = ['name', 'code', 'description']
    success_url = reverse_lazy('organization_list')
