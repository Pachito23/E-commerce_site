# Generated by Django 4.1.2 on 2022-11-17 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0042_alter_customer_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='full_name',
            field=models.CharField(default='hei', max_length=30),
            preserve_default=False,
        ),
    ]
