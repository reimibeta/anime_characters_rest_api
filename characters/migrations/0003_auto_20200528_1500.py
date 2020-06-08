# Generated by Django 2.2.3 on 2020-05-28 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_characterimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characterimages',
            name='character_id',
        ),
        migrations.AddField(
            model_name='characterimages',
            name='characters',
            field=models.ManyToManyField(to='characters.Characters'),
        ),
    ]