# Generated by Django 5.0.1 on 2024-03-10 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0002_housingpost_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="housingpost",
            name="accessibility",
            field=models.TextField(default=None),
        ),
    ]
