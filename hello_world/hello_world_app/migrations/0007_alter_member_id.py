# Generated by Django 4.1.5 on 2023-01-16 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hello_world_app", "0006_alter_member_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
