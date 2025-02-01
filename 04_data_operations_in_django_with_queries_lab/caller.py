import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Student
# Create and check models


def add_students():

    Student.objects.create(
        student_id='FC5204',
        first_name='John',
        last_name='Doe',
        birth_date=date(day=15,month=5,year=1995),
        email='john.doe@university.com',
    )
    Student.objects.create(
        student_id='FE0054',
        first_name='Jane',
        last_name='Smith',
        email='jane.smith@university.com',
    )
    Student.objects.create(
        student_id='FH2014',
        first_name='Alice',
        last_name='Johnson',
        birth_date=date(day=10, month=2,year=1998),
        email='alice.johnson@university.com',
    )

    Student.objects.create(
        student_id='FH2015',
        first_name='Bob',
        last_name='Wilson',
        birth_date=date(day=25,month=11,year=1996),
        email='bob.wilson@university.com',

    )
# Run and print your queries


def get_students_info():
    students_info = []
    for student in Student.objects.all():
        students_info.append(f'Student №{student.student_id}: {student.first_name}'
                             f' {student.last_name}; Email: {student.email}')
    return '\n'.join(students_info)

#print(get_students_info())


def update_students_emails():

    for student in Student.objects.all():
        new_email = student.email.replace("university.com", "uni-students.com")
        student.email = new_email
        student.save()


def truncate_students():
    Student.objects.all().delete()

truncate_students()

print(Student.objects.all())

print(f"Number of students: {Student.objects.count()}")