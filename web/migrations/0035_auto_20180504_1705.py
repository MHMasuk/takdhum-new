# Generated by Django 2.0.3 on 2018-05-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0034_auto_20180504_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takencourse',
            name='view',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
