# Generated by Django 4.1.1 on 2022-10-16 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0006_alter_anime_added_by'),
        ('users', '0006_remove_profile_anime_list_delete_anime'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='aniem_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recommendation.anime'),
        ),
    ]
