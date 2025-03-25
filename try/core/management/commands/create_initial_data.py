from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from faker import Faker
from core.models import College, Program, Organization, Student, OrgMember
import random
from datetime import timedelta

class Command(BaseCommand):
    help = 'Creates initial data with faker'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        # Check if data already exists
        if College.objects.exists():
            self.stdout.write(self.style.WARNING('Data already exists. Skipping...'))
            return

        try:
            with transaction.atomic():
                # Create Colleges
                colleges = []
                college_names = [
                    "College of Engineering",
                    "College of Business",
                    "College of Arts and Sciences",
                    "College of Education",
                    "College of Medicine",
                    "College of Law",
                    "College of Architecture",
                    "College of Computing"
                ]
                for name in college_names:
                    college = College.objects.create(name=name)
                    colleges.append(college)
                self.stdout.write(self.style.SUCCESS(f'Created {len(colleges)} colleges'))

                # Create Programs
                programs = []
                program_prefixes = ['BS', 'BA', 'BEd', 'BSc']
                for college in colleges:
                    for _ in range(random.randint(2, 4)):
                        program = Program.objects.create(
                            name=f"{random.choice(program_prefixes)} in {fake.job()}",
                            college=college
                        )
                        programs.append(program)
                self.stdout.write(self.style.SUCCESS(f'Created {len(programs)} programs'))

                # Create Organizations
                organizations = []
                for college in colleges:
                    for _ in range(2):  # 2 organizations per college
                        org = Organization.objects.create(
                            name=fake.company(),
                            description=fake.paragraph(),
                            college=college
                        )
                        organizations.append(org)
                self.stdout.write(self.style.SUCCESS(f'Created {len(organizations)} organizations'))

                # Create Students
                students = []
                current_year = timezone.now().year
                for _ in range(50):
                    student = Student.objects.create(
                        first_name=fake.first_name(),
                        middle_name=fake.first_name() if random.choice([True, False]) else None,
                        last_name=fake.last_name(),
                        student_id=f"{current_year}-{fake.unique.random_number(digits=4)}",
                        program=random.choice(programs)
                    )
                    students.append(student)
                self.stdout.write(self.style.SUCCESS(f'Created {len(students)} students'))

                # Create OrgMembers
                org_members = []
                current_date = timezone.now().date()
                for student in random.sample(students, 30):  # Make 30 students org members
                    # Only create membership for organizations in student's college
                    valid_orgs = [org for org in organizations if org.college == student.program.college]
                    if valid_orgs:
                        join_date = current_date - timedelta(days=random.randint(0, 365))
                        org_member = OrgMember.objects.create(
                            student=student,
                            organization=random.choice(valid_orgs),
                            date_joined=join_date
                        )
                        org_members.append(org_member)
                self.stdout.write(self.style.SUCCESS(f'Created {len(org_members)} organization members'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
            return

        self.stdout.write(self.style.SUCCESS('Successfully created initial data'))
