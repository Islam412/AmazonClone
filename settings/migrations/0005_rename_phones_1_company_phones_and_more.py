# Generated by Django 4.2 on 2023-09-08 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_remove_company_youtube_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='phones_1',
            new_name='phones',
        ),
        migrations.RemoveField(
            model_name='company',
            name='phones_2',
        ),
    ]
