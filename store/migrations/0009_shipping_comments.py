# Generated by Django 4.1.2 on 2022-11-10 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_rename_state_shipping_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='comments',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
