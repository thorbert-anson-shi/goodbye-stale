# Generated by Django 5.1.1 on 2024-09-17 17:09

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_order_ordereditem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
