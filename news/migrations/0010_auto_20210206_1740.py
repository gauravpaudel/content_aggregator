# Generated by Django 3.1.6 on 2021-02-06 17:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0009_auto_20210206_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='topic',
            name='subscriber',
            field=models.ManyToManyField(related_name='topics', to=settings.AUTH_USER_MODEL),
        ),
    ]
