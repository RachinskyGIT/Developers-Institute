# Generated by Django 4.2 on 2023-04-25 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gifs", "0002_gif_categories_alter_category_gifs"),
    ]

    operations = [
        migrations.RemoveField(model_name="gif", name="categories",),
        migrations.AlterField(
            model_name="category",
            name="gifs",
            field=models.ManyToManyField(
                blank=True, related_name="categories", to="gifs.gif"
            ),
        ),
    ]
