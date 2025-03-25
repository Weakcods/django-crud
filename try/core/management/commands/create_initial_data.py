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