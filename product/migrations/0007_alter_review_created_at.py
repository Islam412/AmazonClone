# Generated by Django 4.2 on 2023-08-30 02:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_slug_alter_review_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 30, 2, 8, 45, 939936, tzinfo=datetime.timezone.utc), verbose_name='Created_at'),
        ),
    ]
