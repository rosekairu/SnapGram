# Generated by Django 3.0.8 on 2020-07-06 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snaps', '0020_auto_20200706_0811'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-last_update']},
        ),
    ]
