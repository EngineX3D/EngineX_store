# Generated by Django 4.0 on 2022-06-25 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='youtube_vid',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='item',
            name='pic_url',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='item',
            name='url',
            field=models.CharField(max_length=500),
        ),
    ]
