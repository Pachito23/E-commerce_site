# Generated by Django 4.1.2 on 2022-11-10 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_shipping_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='shipping',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.shipping'),
        ),
    ]
