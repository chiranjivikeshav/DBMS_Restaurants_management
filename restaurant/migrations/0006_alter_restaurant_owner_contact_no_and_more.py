# Generated by Django 4.2.6 on 2023-11-01 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='owner_contact_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='pin',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='rest_cantact_no',
            field=models.IntegerField(),
        ),
    ]
