# Generated by Django 4.2 on 2023-12-02 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_rename_phones_1_company_phones_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.FloatField()),
            ],
        ),
    ]
