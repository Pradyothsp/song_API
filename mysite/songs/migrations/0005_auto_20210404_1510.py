# Generated by Django 3.1.7 on 2021-04-04 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_auto_20210404_1508'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Audiobook',
            new_name='Audiobooks',
        ),
        migrations.RenameModel(
            old_name='Podcast',
            new_name='Podcasts',
        ),
    ]
