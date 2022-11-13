# Generated by Django 4.1.2 on 2022-11-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_payment_expiration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Sleeping bag', 'Sleeping bag'), ('Jacket', 'Jacket'), ('Accessory', 'Accessory')], default=[('Sleeping bag', 'Sleeping bag')], max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
