from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'college')
    search_fields = ('name',)
    list_filter = ('college',)

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'college')
    search_fields = ('name',)
    list_filter = ('college',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'program')
    search_fields = ('student_id', 'first_name', 'last_name')
    list_filter = ('program',)

@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ('student', 'organization', 'date_joined')
    search_fields = ('student__first_name', 'student__last_name', 'organization__name')
    list_filter = ('organization', 'date_joined')
