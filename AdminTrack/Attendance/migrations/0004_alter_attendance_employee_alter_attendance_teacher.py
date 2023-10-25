# Generated by Django 4.2.6 on 2023-10-24 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Teacher", "0006_alter_teacher_qualifications"),
        ("Employees", "0001_initial"),
        ("Attendance", "0003_attendance_employee_attendance_teacher"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance",
            name="employee",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Employees.employee"
            ),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="teacher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Teacher.teacher"
            ),
        ),
    ]
