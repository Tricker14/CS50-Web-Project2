# Generated by Django 4.2.4 on 2023-09-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_remove_watchlist_product_watchlist_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='product',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to='auctions.auctionlisting'),
        ),
    ]
