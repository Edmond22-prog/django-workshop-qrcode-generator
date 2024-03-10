# Generated by Django 5.0.3 on 2024-03-10 13:45

import website.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('uuid', models.CharField(default=website.utils.generate_uuid, editable=False, max_length=100, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('department', models.CharField(choices=[('IT', 'It'), ('HR', 'Hr'), ('Finance', 'Finance')], default='IT', max_length=20)),
                ('qr_code', models.ImageField(blank=True, editable=False, upload_to='qr_codes/')),
            ],
        ),
    ]