# Generated by Django 3.2 on 2021-05-06 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('title1', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('skills', models.CharField(max_length=50)),
            ],
        ),
    ]
