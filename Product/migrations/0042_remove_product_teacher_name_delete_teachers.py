# Generated by Django 4.2 on 2024-02-27 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0041_remove_product_tpye_lang_alter_product_tutorial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='teacher_name',
        ),
        migrations.DeleteModel(
            name='teachers',
        ),
    ]