# Generated by Django 5.0.7 on 2024-10-16 09:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_studentlist'),
        ('facultyapp', '0003_addcourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcourse',
            name='course',
            field=models.CharField(choices=[('AOOP', 'advanced Object-Oriented Programming'), ('PFSD', 'Python FUll Stack Development')], max_length=50),
        ),
        migrations.AlterField(
            model_name='addcourse',
            name='section',
            field=models.CharField(choices=[('S11', 'SECTION S11'), ('S12', 'SECTION S12'), ('S13', 'SECTION S13'), ('S14', 'SECTION S14'), ('S15', 'SECTION S15')], max_length=50),
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[('AOOP', 'Advanced Object-Oriented Programming'), ('PFSD', 'Python Full Stack Development')], max_length=50)),
                ('marks', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.studentlist')),
            ],
        ),
    ]
