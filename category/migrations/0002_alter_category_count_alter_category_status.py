# Generated by Django 4.1.5 on 2023-02-03 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='count',
            field=models.IntegerField(default=0, verbose_name='تعداد فراخوان'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=False, verbose_name='وضعیت'),
        ),
    ]
