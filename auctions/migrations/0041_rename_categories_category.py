# Generated by Django 4.2.4 on 2023-09-11 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0040_alter_categories_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
    ]