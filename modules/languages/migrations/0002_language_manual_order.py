# Generated by Django 4.0.5 on 2022-06-26 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='manual_order',
            field=models.IntegerField(default=1),
        ),
    ]