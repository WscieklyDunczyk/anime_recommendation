# Generated by Django 4.1.1 on 2022-10-16 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0010_remove_anime_anime_list'),
        ('users', '0010_profile_anime_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='anime_list',
        ),
        migrations.AddField(
            model_name='profile',
            name='anime_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recommendation.anime'),
        ),
    ]