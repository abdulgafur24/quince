from django.db import models
from account.models import User


class Post(models.Model):
    post_title = models.CharField('Название поста', max_length=200)
    post_body = models.TextField('Содержимое поста')
    post_date = models.DateTimeField('Дата публикации')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='Автор публикации')

    def __str__(self):
        return self.post_title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='Автор коментария')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост")
    comment_body = models.CharField('Содержимое коментария', max_length=200)

    def __str__(self):
        # return str(self.comment_author) + ": «" + str(self.comment_body) + "»"
        return str(self.comment_body)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
