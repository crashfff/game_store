# Generated by Django 5.0.3 on 2024-04-01 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='name_of_game',
            name='quantity_purchased',
            field=models.IntegerField(default=0),
        ),
    ]
