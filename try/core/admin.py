from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 20

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'college')
    search_fields = ('name',)
    list_filter = ('college',)
    list_per_page = 20
    raw_id_fields = ('college',)

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'college')
    search_fields = ('name',)
    list_filter = ('college',)
    list_per_page = 20
    raw_id_fields = ('college',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'middle_name', 'last_name', 'program')
    search_fields = ('student_id', 'first_name', 'middle_name', 'last_name')
    list_filter = ('program',)
    list_per_page = 20
    raw_id_fields = ('program',)
    list_select_related = ('program', 'program__college')

@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ('student', 'organization', 'date_joined')
    search_fields = ('student__first_name', 'student__last_name', 'organization__name')
    list_filter = ('organization', 'date_joined')
    list_per_page = 20
    raw_id_fields = ('student', 'organization')
    list_select_related = ('student', 'organization')
