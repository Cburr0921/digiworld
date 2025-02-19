# Generated by Django 5.1.6 on 2025-02-19 21:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_toy_digimon_toys'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDigifarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('digimon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_digifarm', to='main_app.digimon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_digifarm', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DigimonToy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='digimon_toys', to='main_app.toy')),
                ('user_digifarm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='digimon_toys', to='main_app.userdigifarm')),
            ],
        ),
    ]
