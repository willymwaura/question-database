# Generated by Django 4.0.4 on 2022-06-12 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='question',
            field=models.CharField(max_length=100),
        ),
    ]
