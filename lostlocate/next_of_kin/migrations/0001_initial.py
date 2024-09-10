# Generated by Django 4.2.16 on 2024-09-10 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NextOfKin',
            fields=[
                ('next_of_kin_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(default='Unknown', max_length=50)),
                ('relationship', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=15)),
                ('alternative_contact', models.CharField(default='Unknown', max_length=15)),
            ],
        ),
    ]