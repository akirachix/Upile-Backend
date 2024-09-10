# Generated by Django 5.1.1 on 2024-09-09 08:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missing_persons', '0002_alter_missingperson_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='missingperson',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='missingperson',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='missingperson',
            name='last_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='missingperson',
            name='eye_color',
            field=models.CharField(choices=[('black', 'BLACK'), ('brown', 'BROWN')], default='black', max_length=50),
        ),
        migrations.AlterField(
            model_name='missingperson',
            name='skin_color',
            field=models.CharField(choices=[('light_skinned', 'Light Skinned'), ('dark_skinned', 'Dark Skinned')], default='dark_skinned', max_length=50),
        ),
    ]