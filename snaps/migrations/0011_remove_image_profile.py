# Generated by Django 3.0.8 on 2020-07-06 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snaps', '0010_auto_20200706_0607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='profile',
        ),
    ]