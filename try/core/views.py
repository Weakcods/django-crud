from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.utils import OperationalError
from django.contrib.auth import logout
from .models import Student, College, Program, Organization, OrgMember

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

def logout_view(request):
    logout(request)
    return redirect('dashboard')

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

class OrgMemberListView(ListView):
    model = OrgMember
    template_name = 'core/orgmember_list.html'
    context_object_name = 'members'

class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

# Create Views
class StudentCreateView(AdminRequiredMixin, CreateView):
    model = Student
    template_name = 'core/student_form.html'
    fields = ['first_name', 'last_name', 'student_id', 'program']
    success_url = reverse_lazy('student_list')

class CollegeCreateView(AdminRequiredMixin, CreateView):
    model = College
    template_name = 'core/college_form.html'
    fields = ['name', 'code', 'description']
    success_url = reverse_lazy('college_list')

class ProgramCreateView(AdminRequiredMixin, CreateView):
    model = Program
    template_name = 'core/program_form.html'
    fields = ['name', 'code', 'description', 'college']
    success_url = reverse_lazy('program_list')

class OrganizationCreateView(AdminRequiredMixin, CreateView):
    model = Organization
    template_name = 'core/organization_form.html'
    fields = ['name', 'code', 'description']
    success_url = reverse_lazy('organization_list')

class StudentUpdateView(AdminRequiredMixin, UpdateView):
    model = Student
    template_name = 'core/student_form.html'
    fields = ['first_name', 'last_name', 'student_id', 'program']
    success_url = reverse_lazy('student_list')

class StudentDeleteView(AdminRequiredMixin, DeleteView):
    model = Student
    template_name = 'core/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
