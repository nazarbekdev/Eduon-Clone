# Generated by Django 4.2.6 on 2023-11-24 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_lesson_length'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webinar',
            old_name='speakers',
            new_name='user',
        ),
    ]