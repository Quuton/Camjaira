# Generated by Django 4.1.5 on 2023-01-18 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_room_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='lastUpdated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
