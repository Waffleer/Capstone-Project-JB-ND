# Generated by Django 3.2.8 on 2021-10-20 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_rename_code_doc_doccode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='assignmentcode',
            new_name='code',
        ),
    ]
