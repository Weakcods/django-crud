from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from core.models import College, Program, Organization, Student, OrgMember
import random

class Command(BaseCommand):
    help = 'Creates initial data with faker'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        try:
            with transaction.atomic():
                # Create Colleges
                colleges = []
                college_codes = ['CCIS', 'COE', 'COB', 'CAS', 'COEd', 'COM', 'COL', 'COA']
                for i in range(8):
                    college = College.objects.create(
                        name=f"College of {fake.company()}",
                        code=college_codes[i],
                        description=fake.text()
                    )
                    colleges.append(college)
                self.stdout.write(self.style.SUCCESS(f'Created {len(colleges)} colleges'))

                # Create Programs
                programs = []
                program_prefixes = ['BS', 'BA', 'BEd', 'BSc']
                for college in colleges:
                    for _ in range(random.randint(2, 4)):
                        program = Program.objects.create(
                            name=f"{random.choice(program_prefixes)} in {fake.job()}",
                            code=f"{fake.lexify(text='???').upper()}",
                            description=fake.text(),
                            college=college
                        )
                        programs.append(program)
                self.stdout.write(self.style.SUCCESS(f'Created {len(programs)} programs'))

                # Create Organizations
                organizations = []
                for _ in range(10):
                    org = Organization.objects.create(
                        name=fake.company(),
                        code=fake.lexify(text='???').upper(),
                        description=fake.text()
                    )
                    organizations.append(org)
                self.stdout.write(self.style.SUCCESS(f'Created {len(organizations)} organizations'))

                # Create Students
                students = []
                for _ in range(50):
                    student = Student.objects.create(
                        first_name=fake.first_name(),
                        last_name=fake.last_name(),
                        student_id=f"{fake.year()}-{fake.unique.random_number(digits=4)}",
                        program=random.choice(programs)
                    )
                    students.append(student)
                self.stdout.write(self.style.SUCCESS(f'Created {len(students)} students'))