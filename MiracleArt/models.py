from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  # Абстрактная модель
        abstract = True


class Pin(BaseModel):
    title = models.CharField(max_length=30, null=False, blank=False)
    text = models.TextField(max_length=90, null=True, blank=True)
    img = models.ImageField(upload_to='images/', null=False, blank=False)
    slug = models.SlugField(default='', db_index=True)

    def __str__(self):
        return f'Pin {self.id} - {self.title}'

    def get_url(self):
        return reverse('pin_detail', args=[self.id])
