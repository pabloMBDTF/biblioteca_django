# Generated by Django 5.0.1 on 2024-01-31 22:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otraApp', '0002_alter_otrapersona_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('otrapersona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='otraApp.otrapersona')),
                ('puesto', models.CharField(max_length=50, verbose_name='puesto')),
            ],
            bases=('otraApp.otrapersona',),
        ),
    ]