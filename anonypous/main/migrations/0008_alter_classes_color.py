# Generated by Django 3.2.7 on 2021-10-12 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_classcode_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='color',
            field=models.CharField(default='', max_length=15),
        ),
    ]
