# Generated by Django 4.0.10 on 2023-08-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profilepic.jpg', upload_to='profile_pictures'),
        ),
    ]
