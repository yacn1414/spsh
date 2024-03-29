# Generated by Django 4.2 on 2023-05-12 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0032_alter_product_dislikeuser_alter_product_likeuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='dislikeuser',
            field=models.ManyToManyField(blank=True, related_name='+', to='Product.comment', verbose_name='dislikes'),
        ),
        migrations.AlterField(
            model_name='product',
            name='likeuser',
            field=models.ManyToManyField(blank=True, related_name='+', to='Product.comment', verbose_name='likes'),
        ),
    ]
