# Generated by Django 4.2.6 on 2024-06-16 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0015_item_people_rated_alter_item_item_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='item_count',
            field=models.IntegerField(default=1),
        ),
    ]
