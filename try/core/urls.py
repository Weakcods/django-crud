from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('colleges/', views.CollegeListView.as_view(), name='college_list'),
    path('programs/', views.ProgramListView.as_view(), name='program_list'),
    path('organizations/', views.OrganizationListView.as_view(), name='organization_list'),
    path('members/', views.OrgMemberListView.as_view(), name='orgmember_list'),
    
    # Create URLs
    path('student/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('college/create/', views.CollegeCreateView.as_view(), name='college_create'),
    path('program/create/', views.ProgramCreateView.as_view(), name='program_create'),
    path('organization/create/', views.OrganizationCreateView.as_view(), name='organization_create'),

    # Edit and Delete URLs
    path('student/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('student/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('logout/', views.logout_view, name='logout'),
]
