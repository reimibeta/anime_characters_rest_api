# Generated by Django 2.2.3 on 2020-05-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='raw_password',
            field=models.TextField(blank=True),
        ),
    ]