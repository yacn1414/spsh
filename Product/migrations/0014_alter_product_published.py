# Generated by Django 4.1.7 on 2023-02-27 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0013_remove_product_buyers_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='published',
            field=models.BooleanField(default=False, verbose_name='وضعیت'),
        ),
    ]