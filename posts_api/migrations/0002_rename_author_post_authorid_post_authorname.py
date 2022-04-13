# Generated by Django 4.0.3 on 2022-04-13 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='authorID',
        ),
        migrations.AddField(
            model_name='post',
            name='authorName',
            field=models.CharField(default='anonymus user', max_length=64),
        ),
    ]
