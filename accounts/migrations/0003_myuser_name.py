# Generated by Django 4.0.3 on 2022-04-13 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_myuser_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='name',
            field=models.CharField(default='anonymus user', max_length=64, unique=True),
        ),
    ]
