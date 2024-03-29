# Generated by Django 4.1.2 on 2022-11-11 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_remove_payment_card_holder_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='cc_code',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='cc_expiry',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='cc_number',
        ),
        migrations.AddField(
            model_name='payment',
            name='card_holder_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='card_number',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='cvv',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
