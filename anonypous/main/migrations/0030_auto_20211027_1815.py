# Generated by Django 3.2.8 on 2021-10-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20211027_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doc',
            old_name='pointValue',
            new_name='score',
        ),
        migrations.AlterField(
            model_name='doc',
            name='comment',
            field=models.TextField(default=''),
        ),
    ]
