from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=450)    # заголовок
    author = models.ForeignKey(     # автор поста (задаем в административной панели)
        'auth.User',
        on_delete=models.CASCADE,   # удаление поста
    )
    body = models.TextField()   # поле поста

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    middle_name = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

