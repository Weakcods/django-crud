from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from core.models import College, Program, Organization, Student, OrgMember
import random