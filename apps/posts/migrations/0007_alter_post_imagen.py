# Generated by Django 4.2.3 on 2023-08-02 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_creador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
