# Generated by Django 3.2.6 on 2021-08-18 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test2_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='position',
            field=models.CharField(max_length=200),
        ),
    ]
