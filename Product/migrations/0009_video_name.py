# Generated by Django 4.1.5 on 2023-02-07 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0008_alter_video_id_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]