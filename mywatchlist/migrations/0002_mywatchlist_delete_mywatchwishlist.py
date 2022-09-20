# Generated by Django 4.1.1 on 2022-09-20 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyWatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('release_date', models.CharField(max_length=50)),
                ('review', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='MyWatchWishlist',
        ),
    ]
