# Generated by Django 4.2.16 on 2024-09-12 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('police', '0001_initial'),
        ('missing_persons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='missingperson',
            name='officer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='police.policeofficer'),
        ),
    ]
