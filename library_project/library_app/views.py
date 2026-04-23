from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import date, timedelta

from .models import Book, Loan
from .forms import RegisterForm


def index(request):
    query = request.GET.get("q")
    books = Book.objects.filter(title__icontains=query) if query else Book.objects.all()
    return render(request, "index.html", {"books": books})


def book_detail(request, isbn):
    book = get_object_or_404(Book, isbn=isbn)
    return render(request, "book_detail.html", {"book": book})


def user_login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user:
            login(request, user)
            return redirect("index")
        return render(request, "login.html", {"error": "Ошибка входа"})
    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("index")


@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})


# # 🔐 проверка библиотекаря
# def is_librarian(user):
#     return Staff.objects.filter(user=user).exists()


@user_passes_test(is_librarian)
def librarian_dashboard(request):
    loans = Loan.objects.all().order_by("-issue_date")
    return render(request, "librarian/dashboard.html", {"loans": loans})


@user_passes_test(is_librarian)
def issue_book(request):
    if request.method == "POST":
        member = Member.objects.get(id=request.POST["member_id"])
        book = Book.objects.get(isbn=request.POST["isbn"])
        staff = Staff.objects.get(user=request.user)

        if book.available > 0:
            Loan.objects.create(
                member=member,
                book=book,
                staff=staff,
                due_date=date.today() + timedelta(days=14)
            )
            book.available -= 1
            book.save()

    return redirect("librarian_dashboard")


@user_passes_test(is_librarian)
def return_book(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id)

    if not loan.return_date:
        loan.return_date = date.today()
        loan.book.available += 1
        loan.book.save()
        loan.save()

    return redirect("librarian_dashboard")

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