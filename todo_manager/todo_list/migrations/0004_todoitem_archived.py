# Generated by Django 5.1 on 2024-11-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_todoitem_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]