# Generated by Django 2.2 on 2020-07-27 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_article_textfield'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='textfield',
            new_name='full_description',
        ),
    ]
