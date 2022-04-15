# Generated by Django 4.0.3 on 2022-04-15 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts_api', '0007_alter_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='users_who_liked_post',
            field=models.ManyToManyField(related_name='users_liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='authorID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author_set', to=settings.AUTH_USER_MODEL),
        ),
    ]