from datetime import datetime

from django.shortcuts import render
from books.models import Book
from utils.PaginatorSingleton import PaginatorSingleton

def books_view_date(request, pub_date):
    template = 'books/books_list.html'
    pagi = PaginatorSingleton()
    if pagi.is_date(pub_date):
        context = {'books':  pagi.getBooksByDate(pub_date), 'next':  pagi.getNextDate(), 'prev':  pagi.getPreviosDate()}
    else:
        return books_view(request)
    return render(request, template, context)

def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all().order_by('pub_date')}
    return render(request, template, context)



