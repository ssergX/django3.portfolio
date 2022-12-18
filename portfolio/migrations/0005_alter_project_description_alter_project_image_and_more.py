# Generated by Django 4.1.3 on 2022-12-12 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0004_alter_project_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(
                default=" Without img", upload_to="portfolio/images/"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]