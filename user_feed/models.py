from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)

    def __str__(self):
        return 'Юзер: {0}, Имя: {1}, Фамилия: {2},'.format(self.user, self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Профиль юзера'
        verbose_name_plural = 'Профиля юзеров'


class Note(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return 'Название: {0},  Дата создания: {1}, Заметки Юзера: {2}'.format(self.title, self.created_at, self.user)

    class Meta:
        verbose_name = 'Заметки'
        verbose_name_plural = 'Заметки'


class Achievement(models.Model):
    name = models.CharField(max_length=75)
    criteria = models.TextField(max_length=255)
    icon = models.ImageField(upload_to='achievements/')

    def __str__(self):
        return 'Имя очивки: {0}, Критерий: {1},'.format(self.name, self.criteria)
    
    class Meta:
        verbose_name = 'Очивки'
        verbose_name_plural = 'Очивки'


class Advertisement(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='advertisements/')
    link = models.URLField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Название: {0}, Ссылка: {1},'.format(self.title, self.link)

    class Meta:
        verbose_name = 'Рекламное обьявление'
        verbose_name_plural = 'Рекламные обьявление'