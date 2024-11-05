# Generated by Django 4.2.16 on 2024-10-16 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("missing_persons", "0008_alter_missingperson_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="missingperson",
            name="status",
            field=models.CharField(
                choices=[
                    ("missing", "Missing"),
                    ("found", "Found"),
                    ("departed", "Departed"),
                ],
                default="missing",
                max_length=20,
            ),
        ),
    ]