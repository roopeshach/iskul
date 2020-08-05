# Generated by Django 3.0.7 on 2020-06-20 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classroom', '0005_auto_20200617_0723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('guardian_name', models.CharField(max_length=30)),
                ('student_age', models.IntegerField()),
                ('student_dob', models.DateField()),
                ('student_address', models.CharField(max_length=100)),
                ('student_contact', models.CharField(max_length=10)),
                ('student_email', models.EmailField(max_length=100)),
                ('date_of_admission', models.DateField(auto_now_add=True)),
                ('student_photo', models.ImageField(upload_to='')),
                ('student_roll', models.CharField(max_length=10)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Grade')),
            ],
        ),
    ]
