# Generated by Django 2.2.24 on 2021-11-10 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
