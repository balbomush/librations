from django.shortcuts import render
from .models import Book
def book_list(request):
    books=Book.objects.order_by('title')
    return render(request,'book/book_list.html',{'books':books})
def book_show(request,book_id):
    book=Book.objects.get(id=book_id)
    return render()
def remove_book(request,book_id):
    obj=Book.objects.get(id=book_id)
    obj.delete

def names(request):
    return render(request, 'book/base.html', {})
