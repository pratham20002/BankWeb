# Generated by Django 4.0.4 on 2022-05-29 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0008_rename_name_user_firstname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]