# Generated by Django 4.1.4 on 2022-12-18 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="register",
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
                ("Name", models.CharField(max_length=100)),
                ("Phone", models.BigIntegerField()),
                ("Usn", models.CharField(max_length=15)),
                (
                    "sem",
                    models.CharField(
                        choices=[
                            ("First", "first"),
                            ("third", "third"),
                            ("fifth", "fifth"),
                        ],
                        default="useless",
                        max_length=6,
                    ),
                ),
                ("Email", models.CharField(max_length=100)),
                (
                    "Branch",
                    models.CharField(
                        choices=[("AIML", "AI"), ("AIDS", "AD"), ("IS", "IS")],
                        default="useless",
                        max_length=10,
                    ),
                ),
                ("Laptop", models.BooleanField()),
                ("date", models.DateField()),
            ],
        ),
    ]