# Generated by Django 3.1.7 on 2021-12-12 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20211212_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(default='3'),
        ),
    ]
