# Generated by Django 4.0.4 on 2022-05-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TA_Scheduling', '0002_alter_myuser_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=20)),
                ('courseInstructor', models.CharField(max_length=20)),
                ('meetingTime', models.TimeField()),
                ('sectionNum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='discussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labNum', models.IntegerField()),
                ('labTA', models.CharField(max_length=20)),
            ],
        ),
    ]