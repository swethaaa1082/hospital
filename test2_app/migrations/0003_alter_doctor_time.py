# Generated by Django 3.2.6 on 2021-08-18 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test2_app', '0002_alter_doctor_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
