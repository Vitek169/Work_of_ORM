import csv
import unicodedata
# from typing import re
from slugify import slugify
import pandas as pandas
from django.core.management.base import BaseCommand

from main import settings
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass


    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            print(phone)
            phone_obj = Phone(
                name = phone.get('name'),
                price = phone.get('price'),
                image = phone.get('image'),
                release_date = phone.get('release_date'),
                lte_exists = phone.get('lte_exists'),
                slug = slugify( phone.get('name') )
            )
            phone_obj.save()
            print(phone_obj)
            # pd_phones = pandas.read_csv(settings.FILE_PATH, skiprows=0, nrows=1000)
            pass
