# Generated by Django 4.1.3 on 2022-12-03 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users_images', verbose_name='Пин/Картинка'),
        ),
    ]
