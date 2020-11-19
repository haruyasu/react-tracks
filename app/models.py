from django.db import models

class Track(models.Model):
    title = models.CharField('タイトル', max_length=100)
    description = models.TextField('説明', blank=True)
    url = models.URLField('URL')
    created_at = models.DateTimeField('作成日', auto_now_add=True)

    def __str__(self):
        return self.title
