# Generated by Django 3.1.5 on 2021-01-28 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210128_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='deploy',
            field=models.URLField(blank=True, max_length=256, verbose_name='deploy'),
        ),
    ]
