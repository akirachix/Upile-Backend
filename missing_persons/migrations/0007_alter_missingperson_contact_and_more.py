# Generated by Django 4.2.16 on 2024-09-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("missing_persons", "0006_alter_missingperson_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="missingperson",
            name="contact",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="missingperson",
            name="eye_color",
            field=models.CharField(
                choices=[("black", "Black"), ("brown", "Brown")],
                default="black",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="missingperson",
            name="first_name",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="missingperson",
            name="gender",
            field=models.CharField(
                choices=[("male", "Male"), ("female", "Female"), ("other", "Other")],
                default="other",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="missingperson",
            name="hair_color",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="missingperson",
            name="last_name",
            field=models.CharField(default="Unknown", max_length=20),
        ),
        migrations.AlterField(
            model_name="missingperson",
            name="location",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="missingperson",
            name="skin_color",
            field=models.CharField(
                choices=[
                    ("light_skinned", "Light Skinned"),
                    ("dark_skinned", "Dark Skinned"),
                ],
                default="dark_skinned",
                max_length=20,
            ),
        ),
    ]
