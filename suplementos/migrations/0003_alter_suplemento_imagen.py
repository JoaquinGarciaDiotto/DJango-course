# Generated by Django 5.0.3 on 2024-03-13 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suplementos', '0002_alter_suplemento_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suplemento',
            name='imagen',
            field=models.ImageField(height_field=100, upload_to='imagenes/', width_field=100),
        ),
    ]
