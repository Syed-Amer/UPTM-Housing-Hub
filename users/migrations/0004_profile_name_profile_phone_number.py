# Generated by Django 5.0.1 on 2024-03-10 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="name",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name="profile",
            name="phone_number",
            field=models.CharField(default=None, max_length=15),
        ),
    ]