# Generated by Django 4.2.4 on 2023-09-11 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0035_remove_auctionlisting_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]