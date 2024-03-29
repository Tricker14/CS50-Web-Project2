# Generated by Django 4.2.4 on 2023-09-08 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auctionlisting_starting_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='bidder',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='commenter',
        ),
        migrations.AddField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bid_action', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='commenter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comment_action', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
