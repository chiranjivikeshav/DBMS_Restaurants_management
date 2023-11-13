# Generated by Django 4.2.6 on 2023-11-13 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_item_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Contact', models.TextField()),
                ('Email', models.TextField()),
                ('Address', models.TextField()),
                ('BankName', models.TextField()),
                ('BankBranch', models.TextField()),
                ('BankIFSC', models.TextField()),
                ('BankAccount', models.TextField()),
                ('About', models.TextField()),
                ('restaurant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
        ),
    ]