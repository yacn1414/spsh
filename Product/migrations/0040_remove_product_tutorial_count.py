# Generated by Django 4.2 on 2023-08-04 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0039_rename_view_product_viewc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tutorial_count',
        ),
    ]
