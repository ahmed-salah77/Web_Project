# Generated by Django 4.0.4 on 2022-05-25 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_alter_course_department_alter_student_active_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='student',
            table='studentdetails',
        ),
    ]
