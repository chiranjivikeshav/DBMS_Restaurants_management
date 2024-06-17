# Generated by Django 4.2.6 on 2024-06-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0014_item_item_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='people_rated',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
    ]