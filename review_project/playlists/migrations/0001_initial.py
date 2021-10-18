# Generated by Django 3.2.8 on 2021-10-17 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('establishments', '0002_alter_establishment_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('establishment', models.ManyToManyField(blank=True, null=True, related_name='rel_to_list', to='establishments.Establishment')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]