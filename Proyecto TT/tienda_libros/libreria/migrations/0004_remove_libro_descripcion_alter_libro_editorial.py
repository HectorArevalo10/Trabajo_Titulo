# Generated by Django 5.0.1 on 2024-07-23 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_libro_descripcion_libro_editorial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='libro',
            name='editorial',
            field=models.CharField(max_length=200),
        ),
    ]
