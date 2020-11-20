from django.db import models
from django.contrib.auth import get_user_model


class Track(models.Model):
    title = models.CharField('タイトル', max_length=100)
    description = models.TextField('説明', blank=True)
    url = models.URLField('URL')
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    posted_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
