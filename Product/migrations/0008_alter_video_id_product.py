# Generated by Django 4.1.5 on 2023-02-07 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='id_Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Product.product', verbose_name='آیدی محصول'),
        ),
    ]
