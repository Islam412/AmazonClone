# Generated by Django 4.2 on 2023-12-05 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='4B6KF9RC', max_length=20),
        ),
    ]