# Generated by Django 3.0.8 on 2020-07-09 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snaps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(default='https://res.cloudinary.com/hpxmrlhxr/image/upload/v1594264002/media/profile_photo/profile_my6l6z.png', upload_to='profile_photo/'),
        ),
    ]