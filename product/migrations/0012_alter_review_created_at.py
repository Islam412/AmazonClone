# Generated by Django 4.2 on 2023-09-05 01:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_review_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 5, 1, 53, 16, 646058, tzinfo=datetime.timezone.utc), verbose_name='Created_at'),
        ),
    ]
