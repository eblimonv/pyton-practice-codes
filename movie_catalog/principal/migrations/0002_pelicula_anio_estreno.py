# Generated by Django 3.1.3 on 2020-11-17 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='anio_estreno',
            field=models.IntegerField(null=True),
        ),
    ]
