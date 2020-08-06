from django.db import models


STATUS_CHOICES = [
    ('new', 'новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано')
]

TYPE_CHOICES = [
    ('task','задача'),
    ('Bug','ошибка'),
    ('Enhancement','улучшение.')
]



class Article(models.Model):

    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    full_description = models.TextField(max_length=3000, null=False, verbose_name='Подробное описание')
    status = models.CharField(max_length=25, choices=STATUS_CHOICES,null=True, default='new', verbose_name='статус')
    type = models.CharField(max_length=25, choices=TYPE_CHOICES,null=True, default='task', verbose_name='тип задачи')
    date = models.CharField(max_length=25, null=False, blank=False, verbose_name='data')

    updated_at = models.DateTimeField(max_length=25, auto_now=True, verbose_name='Время создания')

    def __str__(self):
        return "{}. {}".format(self.pk, self.description)



class Comment(models.Model):
    article = models.ForeignKey('webapp.Article', related_name='comments',
    on_delete=models.CASCADE, verbose_name='Статья')
    text = models.TextField(max_length=400, verbose_name='Комментарий')
    author = models.CharField(max_length=40, null=True, blank=True,
    default='Аноним', verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.text[:20]
