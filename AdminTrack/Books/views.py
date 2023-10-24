from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth import authenticate, login, user_logged_out
from .models import Book
from .forms import BookForm

# Create your views here.
"""
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid username or password'})
    return render(request, 'admin_login.html')

def logout(request):
    logout(request)
    return redirect('login')
"""

def view_books(request):
    """Function to allow admin view list of teachers"""
    books = Book.objects.all()
    context = {
        "books": books,
    }
    return render(request, 'books/view_books.html', context)

def edit_book(request, id):
    """function for admin to edit teacher information"""
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('view_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form, 'book':book})

def delete_book(request, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    return redirect('view_books')

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_books')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})
    