# Generated by Django 2.0.3 on 2018-05-04 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0046_auto_20180504_2102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='takencourse',
            old_name='taken_course_url',
            new_name='taken_course',
        ),
    ]
