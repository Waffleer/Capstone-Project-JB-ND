# Generated by Django 3.2.7 on 2021-11-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_alter_assignmentobj_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentobj',
            name='tags',
            field=models.ManyToManyField(blank=True, to='main.assignmentTags'),
        ),
    ]
