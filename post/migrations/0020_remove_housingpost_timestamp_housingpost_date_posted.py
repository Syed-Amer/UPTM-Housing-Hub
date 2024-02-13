# Generated by Django 5.0.1 on 2024-02-13 12:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0019_remove_housingpost_images_delete_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="housingpost",
            name="timestamp",
        ),
        migrations.AddField(
            model_name="housingpost",
            name="date_posted",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]