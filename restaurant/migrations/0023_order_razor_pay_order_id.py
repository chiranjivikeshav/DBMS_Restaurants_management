# Generated by Django 4.2.6 on 2024-06-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0022_rename_ratingreviews_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='razor_pay_order_id',
            field=models.TextField(default='aaaa'),
            preserve_default=False,
        ),
    ]
