from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
    """Модель ссылки"""

    title = models.CharField(max_length=512, verbose_name="заголовок страницы", blank=True)
    description = models.TextField(verbose_name="краткое описание", blank=True)
    link = models.URLField(max_length=512,  verbose_name="ссылка на страницу", blank=True)
    image = models.URLField(blank=True, null=True, verbose_name="изображение")
    type = models.CharField(max_length=512, verbose_name="тип страницы", default='website', blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    collection_id = models.ManyToManyField("Collection", verbose_name="коллекции", blank= True)

    def __str__(self):
        return self.title

class Collection(models.Model):
    """Модель коллекций"""

    name = models.CharField(max_length=512, verbose_name="назавание")
    description = models.TextField(verbose_name="краткое описание", blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    links = models.ManyToManyField(Link, verbose_name="ссылки", blank=True)

    def __str__(self):
        return self.name
