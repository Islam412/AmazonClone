# Generated by Django 4.2 on 2023-09-08 06:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_review_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 8, 6, 29, 5, 222698, tzinfo=datetime.timezone.utc), verbose_name='Created_at'),
        ),
    ]