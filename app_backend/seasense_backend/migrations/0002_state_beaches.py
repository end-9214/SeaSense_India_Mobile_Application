# Generated by Django 5.1.2 on 2024-10-27 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("seasense_backend", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="state",
            name="beaches",
            field=models.TextField(blank=True, null=True),
        ),
    ]
