# Generated by Django 3.2.8 on 2021-10-20 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20211019_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doc',
            old_name='code',
            new_name='doccode',
        ),
    ]
