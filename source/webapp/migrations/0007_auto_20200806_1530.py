# Generated by Django 2.2 on 2020-08-06 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20200806_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('new', 'новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')], default='new', max_length=25, null=True, verbose_name='статус'),
        ),
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.CharField(choices=[('task', 'задача'), ('Bug', 'ошибка'), ('Enhancement', 'улучшение.')], default='task', max_length=25, null=True, verbose_name='тип задачи'),
        ),
    ]