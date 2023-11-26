# Generated by Django 4.2.6 on 2023-11-23 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_lesson_video_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_thumbnail',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.level'),
        ),
        migrations.AlterField(
            model_name='course',
            name='trailer',
            field=models.FileField(upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='thumbnail',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video_location',
            field=models.FileField(upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='webinar',
            name='thumbnail',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='webinar',
            name='trailer',
            field=models.FileField(upload_to='videos/'),
        ),
    ]