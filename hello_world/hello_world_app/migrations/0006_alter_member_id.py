# Generated by Django 4.1.5 on 2023-01-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hello_world_app", "0005_alter_member_joined_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
