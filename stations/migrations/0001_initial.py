# Generated by Django 4.2 on 2024-09-14 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PoliceStation",
            fields=[
                (
                    "station_id",
                    models.SmallIntegerField(primary_key=True, serialize=False),
                ),
                ("station_name", models.CharField(max_length=50)),
                ("location", models.CharField(max_length=50)),
            ],
        ),
    ]
