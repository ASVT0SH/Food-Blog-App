# Generated by Django 4.0.10 on 2023-08-19 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_img',
            field=models.CharField(default='data:image/jpeg;base64,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', max_length=500),
        ),
    ]
