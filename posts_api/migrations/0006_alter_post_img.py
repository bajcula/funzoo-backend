# Generated by Django 4.0.3 on 2022-04-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_api', '0005_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='post_images'),
        ),
    ]
