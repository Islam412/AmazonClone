# Generated by Django 4.2 on 2023-10-09 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_alter_order_code_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='IWJEOHFW', max_length=20),
        ),
    ]
