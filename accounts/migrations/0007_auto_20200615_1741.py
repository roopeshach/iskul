# Generated by Django 3.0.3 on 2020-06-15 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_content_topic'),
        ('accounts', '0006_auto_20200615_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grades',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Grade'),
        ),
    ]