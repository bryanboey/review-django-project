# Generated by Django 3.2.8 on 2021-10-17 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0002_alter_establishment_options'),
        ('playlists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='establishment',
            field=models.ManyToManyField(blank=True, related_name='rel_to_list', to='establishments.Establishment'),
        ),
    ]