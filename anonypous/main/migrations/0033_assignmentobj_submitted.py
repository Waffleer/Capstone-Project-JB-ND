# Generated by Django 3.2.9 on 2021-11-17 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_assignmentobj_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentobj',
            name='submitted',
            field=models.BooleanField(default=False),
        ),
    ]
