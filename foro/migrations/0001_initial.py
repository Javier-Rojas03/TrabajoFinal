# Generated by Django 4.2.7 on 2023-11-14 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('artista', models.CharField(max_length=20)),
                ('titulo', models.CharField(max_length=30)),
                ('subtitulo', models.CharField(max_length=100)),
                ('opinion', models.TextField()),
                ('puntaje', models.DecimalField(decimal_places=1, max_digits=3)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('director', models.CharField(max_length=20)),
                ('titulo', models.CharField(max_length=30)),
                ('subtitulo', models.CharField(max_length=100)),
                ('opinion', models.TextField()),
                ('puntaje', models.DecimalField(decimal_places=1, max_digits=3)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Videojuego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('desarrollador', models.CharField(max_length=20)),
                ('titulo', models.CharField(max_length=30)),
                ('subtitulo', models.CharField(max_length=100)),
                ('opinion', models.TextField()),
                ('puntaje', models.DecimalField(decimal_places=1, max_digits=3)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
