# Generated by Django 4.2 on 2024-02-28 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0010_alter_historicaltransfer_purchase_history_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltransfer_purchase_history',
            name='amount_send',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicaltransfer_purchase_history',
            name='price_Pur',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transfer_purchase_history',
            name='amount_send',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transfer_purchase_history',
            name='price_Pur',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
