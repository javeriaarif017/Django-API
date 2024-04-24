# Generated by Django 4.2.9 on 2024-01-05 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CameraData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.CharField(max_length=1000)),
                ('captured_at', models.CharField(max_length=1000)),
                ('updated_at', models.CharField(max_length=1000)),
                ('created_at', models.CharField(max_length=1000)),
                ('camera_id', models.CharField(max_length=1000)),
                ('file_url', models.CharField(max_length=1000)),
                ('specie_id', models.CharField(max_length=1000)),
                ('Date', models.CharField(max_length=1000)),
                ('Time', models.CharField(max_length=1000)),
            ],
        ),
    ]