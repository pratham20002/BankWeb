# Generated by Django 4.0.4 on 2022-05-29 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0007_rename_firstname_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='firstname',
        ),
    ]
