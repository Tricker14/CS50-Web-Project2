# Generated by Django 4.2.4 on 2023-09-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0051_alter_auctionlisting_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='starting_bid',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
