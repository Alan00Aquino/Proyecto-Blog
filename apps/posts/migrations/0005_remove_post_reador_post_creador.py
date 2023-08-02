# Generated by Django 4.2.3 on 2023-07-31 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_post_reador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='reador',
        ),
        migrations.AddField(
            model_name='post',
            name='creador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posteos_usario', to=settings.AUTH_USER_MODEL),
        ),
    ]