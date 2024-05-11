# Generated by Django 4.2.13 on 2024-05-11 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=100)),
                (
                    "cover_image",
                    models.ImageField(blank=True, null=True, upload_to="covers/"),
                ),
                ("duration", models.DurationField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name="Chapter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("audio_file", models.FileField(upload_to="chapters/")),
                ("duration", models.IntegerField(default=0, editable=False)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chapters",
                        to="books.book",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ListeningProgress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("last_position", models.IntegerField(default=0)),
                ("total_listened", models.IntegerField(default=0)),
                (
                    "chapter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="progress",
                        to="books.chapter",
                    ),
                ),
            ],
        ),
    ]
