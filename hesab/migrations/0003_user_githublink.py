# Generated by Django 4.2 on 2023-05-16 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hesab', '0002_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='githublink',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
