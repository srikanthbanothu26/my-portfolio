# Generated by Django 5.0.6 on 2024-07-05 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0002_alter_school_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.TextField(default=None)),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='Resume.detail')),
            ],
        ),
    ]
