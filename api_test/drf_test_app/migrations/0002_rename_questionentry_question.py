# Generated by Django 4.0.2 on 2022-03-24 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drf_test_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuestionEntry',
            new_name='Question',
        ),
    ]
