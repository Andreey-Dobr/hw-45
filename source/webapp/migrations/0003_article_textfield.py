# Generated by Django 2.2 on 2020-07-27 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200723_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='textfield',
            field=models.TextField(default=1, max_length=3000, verbose_name='Подробное описание'),
            preserve_default=False,
        ),
    ]
