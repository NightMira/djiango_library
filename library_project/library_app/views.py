from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import date, timedelta

from .models import Book, Loan, User
from .forms import RegisterForm


# ------------------------
# КНИГИ
# ------------------------

def index(request):
    query = request.GET.get("q")
    books = Book.objects.filter(title__icontains=query) if query else Book.objects.all()
    return render(request, "index.html", {"books": books})


def book_detail(request, isbn):
    book = get_object_or_404(Book, isbn=isbn)
    return render(request, "book_detail.html", {"book": book})


# ------------------------
# АВТОРИЗАЦИЯ (Django auth)
# ------------------------

@login_required
def borrow_book(request, isbn):
    book = get_object_or_404(Book, isbn=isbn)

    already_borrowed = Loan.objects.filter(
        user=request.user,
        book=book,
        return_date__isnull=True
    ).exists()

    if book.available > 0 and not already_borrowed:
        Loan.objects.create(
            user=request.user,
            book=book,
            due_date=date.today() + timedelta(days=14)
        )

        book.available -= 1
        book.save()

    return redirect("profile")

@login_required
def profile(request: HttpRequest) -> HttpResponse:
    loans = Loan.objects.filter(user=request.user, return_date__isnull=True)

    return render(request, 'profile.html', {
        'user': request.user,
        'loans': loans
    })


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# ------------------------
# РОЛИ
# ------------------------

def is_librarian(user):
    return user.is_authenticated and user.role == "librarian"


# ------------------------
# БИБЛИОТЕКАРЬ
# ------------------------

@user_passes_test(is_librarian)
def librarian_dashboard(request):
    loans = Loan.objects.all().order_by("-issue_date")
    return render(request, "librarian/dashboard.html", {"loans": loans})


@user_passes_test(is_librarian)
def issue_book(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        isbn = request.POST.get("isbn")

        if not user_id or not isbn:
            return redirect("librarian_dashboard")

        try:
            user = User.objects.get(id=user_id)
            book = Book.objects.get(isbn=isbn)

            if book.available > 0:
                Loan.objects.create(
                    user=user,
                    book=book,
                    due_date=date.today() + timedelta(days=14)
                )

                book.available -= 1
                book.save()

        except (User.DoesNotExist, Book.DoesNotExist):
            pass

    return redirect("librarian_dashboard")


@user_passes_test(is_librarian)
def return_book(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id)

    if loan.return_date is None:
        loan.return_date = date.today()
        loan.book.available += 1
        loan.book.save()
        loan.save()

    return redirect("librarian_dashboard")