from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Book
from .forms import BookForm
from django.contrib import messages
from django.db.models.base import ObjectDoesNotExist
def Dostoevsky(request):
 names = Book.objects.filter(author='Достоевский').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Gogol(request):
 names = Book.objects.filter(author='Гоголь').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Lovecraft(request):
 names = Book.objects.filter(author='Лавкрафт').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Chehov(request):
 names = Book.objects.filter(author='Чехов').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Kafka(request):
 names = Book.objects.filter(author='Кафка').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Gugo(request):
 names = Book.objects.filter(author='Гюго').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Hemingway(request):
 names = Book.objects.filter(author='Хемингуэй').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Bulgakov(request):
 names = Book.objects.filter(author='Булгаков').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Lermontov(request):
 names = Book.objects.filter(author='Лермонтов').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Remark(request):
 names = Book.objects.filter(author='Ремарк').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Gesse(request):
 names = Book.objects.filter(author='Гессе').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Gork(request):
 names = Book.objects.filter(author='Горький').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Twain (request):
 names = Book.objects.filter(author='Твен').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Asimov(request):
 names = Book.objects.filter(author='Азимов').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Pratchet(request):
 names = Book.objects.filter(author='Пратчетт').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Bradbury(request):
 names = Book.objects.filter(author='Брэдбери').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Bukowski(request):
 names = Book.objects.filter(author='Буковски').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Grin(request):
 names = Book.objects.filter(author='Грин').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Nabokov(request):
 names = Book.objects.filter(author='Набоков').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Soldj(request):
 names = Book.objects.filter(author='Солженицын').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def King(request):
 names = Book.objects.filter(author='Кинг').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})
def Bunin(request):
 names = Book.objects.filter(author='Бунин').order_by('published_date')
 return render(request, 'book/name.html', {'names': names})

def book_list(request):
    books = Book.objects.all()
    return render(request,'book/book_list.html',{'books':books})


def book_show(request,book_id):
    try:
        book=Book.objects.get(id=book_id)
    except ObjectDoesNotExist:
         messages.error(request, "This book does not exist")
         return redirect('/')
    return render()



def remove_book(request,book_id):
    obj=Book.objects.get(id=book_id)
    obj.delete
    messages.success(request,'The Book has been successfully removed')
    return redirect('/')


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
