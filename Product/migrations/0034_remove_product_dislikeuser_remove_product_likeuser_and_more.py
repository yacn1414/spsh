# Generated by Django 4.2 on 2023-05-12 19:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Product', '0033_alter_product_dislikeuser_alter_product_likeuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='dislikeuser',
        ),
        migrations.RemoveField(
            model_name='product',
            name='likeuser',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='like',
        ),
        migrations.AddField(
            model_name='comment',
            name='dislike',
            field=models.ManyToManyField(blank=True, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='dislikes'),
        ),
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='likes'),
        ),
    ]