# Generated by Django 4.2.6 on 2023-10-24 10:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="availabilityStatus",
            field=models.CharField(
                blank=True,
                choices=[
                    ("available", "Available"),
                    ("checked_out", "Checked Out"),
                    ("reserved", "Reserved"),
                    ("lost", "Lost"),
                    ("damaged", "Damaged"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]
