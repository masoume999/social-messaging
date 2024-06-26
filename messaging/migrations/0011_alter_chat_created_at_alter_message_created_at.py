# Generated by Django 4.2.9 on 2024-02-04 19:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("messaging", "0010_alter_chat_created_at_alter_message_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chat",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 2, 4, 19, 21, 45, 323403, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 2, 4, 19, 21, 45, 324404, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
