from django.db import models

from users.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  # Абстрактная модель
        abstract = True


class PinCategory(BaseModel):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Pin Categories'

    def __str__(self):
        return self.name


class Pin(BaseModel):
    title = models.CharField(max_length=30, null=False, blank=False)
    text = models.TextField(max_length=90, null=True, blank=True)
    img = models.ImageField(upload_to='images/', null=False, blank=False)
    slug = models.SlugField(default='', db_index=True)
    category = models.ForeignKey(PinCategory, on_delete=models.PROTECT, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Pin {self.id} - {self.title}'

    def get_url(self):
        return reverse('pin_detail', args=[self.id])
