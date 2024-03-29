# Generated by Django 4.1.7 on 2023-03-04 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0018_product_teacher_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tutorial_level',
            field=models.CharField(choices=[('junior', 'مبتدی'), ('mid-level', 'متوسط'), ('sinior', 'حرفه ای')], default='junior', max_length=100, verbose_name='سطح دوره'),
        ),
        migrations.AlterField(
            model_name='product',
            name='published',
            field=models.BooleanField(default=True, verbose_name='وضعیت'),
        ),
    ]
