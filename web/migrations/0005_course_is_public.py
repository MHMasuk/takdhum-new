# Generated by Django 2.0.3 on 2018-03-20 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20180319_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]