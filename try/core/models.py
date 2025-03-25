from django.db import models
from django.core.exceptions import ValidationError

class College(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Colleges'

class Program(models.Model):
    name = models.CharField(max_length=100)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        unique_together = ['name', 'college']

class Organization(models.Model):
    name = models.CharField(max_length=100)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        unique_together = ['name', 'college']

    def clean(self):
        if len(self.description.strip()) < 10:
            raise ValidationError('Description must be at least 10 characters long')

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=20, unique=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.middle_name or ''} {self.last_name}".strip()

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_full_name(self):
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        if not self.student_id.strip():
            raise ValidationError('Student ID cannot be empty')

class OrgMember(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    date_joined = models.DateField(verbose_name="Date Joined")

    def __str__(self):
        return f"{self.student} - {self.organization}"

    class Meta:
        ordering = ['-date_joined']
        unique_together = ['student', 'organization']

    def clean(self):
        if self.student.program.college != self.organization.college:
            raise ValidationError("Student's college must match organization's college")
