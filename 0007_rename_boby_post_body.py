# Generated by Django 3.2 on 2021-05-14 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_reviews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='boby',
            new_name='body',
        ),
    ]
