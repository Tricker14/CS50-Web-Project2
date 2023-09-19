# Generated by Django 4.2.4 on 2023-09-09 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auctionlisting_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auction_bidder', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='image_URL',
            field=models.URLField(blank=True, null=True),
        ),
    ]