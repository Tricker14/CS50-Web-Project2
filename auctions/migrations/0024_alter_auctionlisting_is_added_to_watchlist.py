# Generated by Django 4.2.4 on 2023-09-10 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_auctionlisting_is_added_to_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='is_added_to_watchlist',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]