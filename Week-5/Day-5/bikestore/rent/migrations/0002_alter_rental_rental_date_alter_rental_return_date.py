# Generated by Django 4.2 on 2023-04-28 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rent", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rental",
            name="rental_date",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="rental",
            name="return_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]