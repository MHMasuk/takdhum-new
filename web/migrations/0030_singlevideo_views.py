# Generated by Django 2.0.3 on 2018-05-03 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0029_auto_20180429_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='singlevideo',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]