# Generated by Django 4.1.4 on 2024-01-25 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_alter_libro_categoria'),
        ('lector', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libroPrestamo', to='libro.libro'),
        ),
    ]