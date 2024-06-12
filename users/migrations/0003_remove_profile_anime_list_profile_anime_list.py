# Generated by Django 4.1.1 on 2022-10-10 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_anime_profile_anime_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='anime_list',
        ),
        migrations.AddField(
            model_name='profile',
            name='anime_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.anime'),
        ),
    ]
