# Generated by Django 4.1.1 on 2022-10-16 11:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recommendation', '0006_alter_anime_added_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='added_by',
        ),
        migrations.AddField(
            model_name='anime',
            name='anime_list',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
