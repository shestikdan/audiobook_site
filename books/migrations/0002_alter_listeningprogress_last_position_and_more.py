# Generated by Django 4.2.13 on 2024-05-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listeningprogress",
            name="last_position",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="listeningprogress",
            name="total_listened",
            field=models.IntegerField(default=0),
        ),
    ]
