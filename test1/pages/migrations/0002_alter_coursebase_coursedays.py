# Generated by Django 4.0.4 on 2022-05-22 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursebase',
            name='courseDays',
            field=models.IntegerField(),
        ),
    ]
