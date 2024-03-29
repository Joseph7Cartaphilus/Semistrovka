from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from users.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  # Абстрактная модель
        abstract = True


class PinCategory(BaseModel):
    name = models.CharField(max_length=64, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name


class Pin(BaseModel):
    title = models.CharField(max_length=30, null=False, blank=False, verbose_name='Название')
    text = models.TextField(max_length=90, null=True, blank=True, verbose_name='Описание')
    img = models.ImageField(upload_to='images/', null=False, blank=False, verbose_name='Пин/Картинка')
    slug = models.SlugField(default='', db_index=True, verbose_name='слаг')
    category = models.ForeignKey(PinCategory, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Категория')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f'Pin {self.id} - {self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Pin, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('pin_detail_slug_id', args=[self.slug, self.id])
