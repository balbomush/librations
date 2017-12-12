from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Book
from .forms import BookForm


def book_list(request):
    books = Book.objects.all()
    return render(request,'book/book_list.html',{'books':books})


def book_show(request,book_id):
    book=Book.objects.get(id=book_id)
    return render()


def remove_book(request,book_id):
    obj=Book.objects.get(id=book_id)
    obj.delete


def names(request):
    return render(request, 'book/base.html', {})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})

def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'book/book_new.html', {'form': form})

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'book/book_edit.html', {'form': form})
