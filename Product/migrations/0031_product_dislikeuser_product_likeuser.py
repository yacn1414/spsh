# Generated by Django 4.2 on 2023-05-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0030_comment_dislike_comment_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dislikeuser',
            field=models.ManyToManyField(related_name='+', to='Product.comment', verbose_name='dislikes'),
        ),
        migrations.AddField(
            model_name='product',
            name='likeuser',
            field=models.ManyToManyField(related_name='+', to='Product.comment', verbose_name='likes'),
        ),
    ]
