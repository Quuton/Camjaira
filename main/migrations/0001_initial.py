# Generated by Django 4.1.7 on 2023-03-30 03:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('floor', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, default='room_images/placeholder.png', upload_to='room_images')),
                ('size', models.IntegerField()),
                ('price', models.FloatField()),
                ('availability', models.BooleanField(default=True)),
                ('visitCount', models.IntegerField(default=0)),
                ('lastUpdated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True)),
                ('favourite', models.BooleanField(default=False)),
                ('timeStamp', models.DateTimeField(auto_now=True)),
                ('resolved', models.BooleanField(default=False)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoomAmenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('roomID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.room')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cleanlinessRating', models.IntegerField()),
                ('aestheticRating', models.IntegerField()),
                ('comfortRating', models.IntegerField()),
                ('valueRating', models.IntegerField()),
                ('comment', models.TextField(blank=True)),
                ('timeStamp', models.DateTimeField(auto_now=True)),
                ('roomID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.room')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('scheduledDate', models.DateField()),
                ('topic', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True)),
                ('ipAddress', models.GenericIPAddressField()),
                ('timeStamp', models.DateTimeField(auto_now=True)),
                ('resolved', models.BooleanField(default=False)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
