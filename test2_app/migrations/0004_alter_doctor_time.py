# Generated by Django 3.2.6 on 2021-08-18 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test2_app', '0003_alter_doctor_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='time',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
