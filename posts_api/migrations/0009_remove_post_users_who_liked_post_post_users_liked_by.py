# Generated by Django 4.0.3 on 2022-04-15 17:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts_api', '0008_post_users_who_liked_post_alter_post_authorid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='users_who_liked_post',
        ),
        migrations.AddField(
            model_name='post',
            name='users_liked_by',
            field=models.ManyToManyField(related_name='users_liked_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
