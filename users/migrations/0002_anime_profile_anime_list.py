# Generated by Django 4.1.1 on 2022-10-10 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('anime_type', models.CharField(max_length=10)),
                ('episodes', models.IntegerField()),
                ('status', models.CharField(max_length=15)),
                ('aired', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='anime_thumbnail')),
                ('synopsis', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='anime_list',
            field=models.ManyToManyField(blank=True, to='users.anime'),
        ),
    ]
