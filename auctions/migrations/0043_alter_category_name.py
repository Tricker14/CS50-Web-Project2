# Generated by Django 4.2.4 on 2023-09-11 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0042_remove_category_product_auctionlisting_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
