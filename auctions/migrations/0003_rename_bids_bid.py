# Generated by Django 4.2.4 on 2023-09-06 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auctionlisting_bids'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bids',
            new_name='Bid',
        ),
    ]
