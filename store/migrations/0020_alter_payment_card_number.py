# Generated by Django 4.1.2 on 2022-11-11 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_remove_payment_cc_code_remove_payment_cc_expiry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=models.CharField(default='1234567891234567', max_length=30, null=True),
        ),
    ]