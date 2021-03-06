# Generated by Django 3.2.8 on 2021-10-25 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0025_assignmentobj_submissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='submissions',
            field=models.ManyToManyField(blank=True, to='main.documentcode'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
