# Generated by Django 4.0.4 on 2022-05-03 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TA_Scheduling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='userType',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Instructor', 'Instructor'), ('TA', 'Ta')], default='TA', max_length=10),
        ),
    ]
