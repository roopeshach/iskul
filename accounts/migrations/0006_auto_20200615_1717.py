# Generated by Django 3.0.3 on 2020-06-15 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_content_uploaded_by'),
        ('accounts', '0005_teacher_grades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='grades',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Grade'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Subject'),
        ),
    ]
