# Generated by Django 4.1.1 on 2022-10-16 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_aniem_list_profile_anime_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='anime_list',
        ),
    ]