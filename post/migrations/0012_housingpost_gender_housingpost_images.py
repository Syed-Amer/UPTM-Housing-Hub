# Generated by Django 5.0.1 on 2024-02-12 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0011_alter_housingpost_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="housingpost",
            name="gender",
            field=models.CharField(
                choices=[("male", "Male"), ("female", "Female")],
                default=None,
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="housingpost",
            name="images",
            field=models.ImageField(
                blank=True, null=True, upload_to="housing_post_images/"
            ),
        ),
    ]