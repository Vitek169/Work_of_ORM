from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=100, default='')
    price = models.FloatField(default=0.00)
    image = models.CharField(max_length=255, default='')
    release_date = models.DateField(default='1900-01-01')
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, default='')
