# Generated by Django 3.1.5 on 2021-01-28 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210128_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='github',
            field=models.URLField(blank=True, max_length=256, verbose_name='github'),
        ),
    ]
