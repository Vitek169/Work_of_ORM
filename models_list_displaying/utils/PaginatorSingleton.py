import pandas
from django.core.paginator import Paginator
from dateutil.parser import parse
# from pagination import settings
from books.models import Book


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class PaginatorSingleton(metaclass=MetaSingleton):
    pub_date = None

    def getBooksByDate(self, pub_date):
        if not pub_date is None:
            self.pub_date = pub_date
            self.books = Book.objects.filter(pub_date=pub_date).order_by('pub_date')
        return self.books

    def getPreviosDate(self):
        book = Book.objects.filter(pub_date__lt=self.pub_date)#.order_by('pub_date')
        print(book)
        if book:
            return book[0].pub_date.strftime('%Y-%m-%d')
        else:
            return None

    def getNextDate(self):
        book = Book.objects.filter(pub_date__gt=self.pub_date)#.order_by('pub_date')
        print(book)
        if book:
            return book[0].pub_date.strftime('%Y-%m-%d')
        else:
            return None
    @staticmethod
    def is_date(string, fuzzy=False):
        try:
            parse(string, fuzzy=fuzzy)
            return True

        except ValueError:
            return False
