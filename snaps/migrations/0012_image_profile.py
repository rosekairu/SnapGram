# Generated by Django 3.0.8 on 2020-07-06 03:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('snaps', '0011_remove_image_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='snaps.Profile'),
            preserve_default=False,
        ),
    ]