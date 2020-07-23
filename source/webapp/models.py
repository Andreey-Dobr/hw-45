from django.db import models


STATUS_CHOICES = [
    ('new', 'новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано')
]



class Article(models.Model):

    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='new', verbose_name='статус')

    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return "{}. {}".format(self.pk, self.description)
