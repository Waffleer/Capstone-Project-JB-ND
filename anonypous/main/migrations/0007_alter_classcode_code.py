# Generated by Django 3.2.8 on 2021-10-11 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20211011_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classcode',
            name='code',
            field=models.CharField(max_length=6),
        ),
    ]
