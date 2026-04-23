from django.db import models
from django.contrib.auth.models import User

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)  # login
    email = models.EmailField(unique=True)

    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, blank=True)

    ROLE_CHOICES = [
        ('reader', 'Reader'),
        ('librarian', 'Librarian'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='reader')

    date_reg = models.DateTimeField(auto_now_add=True)

class Author(models.Model):
    full_name = models.CharField(max_length=150)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    isbn = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=255)

    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    year = models.IntegerField(blank=True, null=True)
    copies = models.IntegerField(default=1)
    available = models.IntegerField(default=1)

    def __str__(self):
        return self.title

# class Member(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=150)
#     address = models.CharField(max_length=200, blank=True)
#     phone = models.CharField(max_length=20, blank=True)
#     registration_date = models.DateField(auto_now_add=True)


# class Staff(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     full_name = models.CharField(max_length=150)
#     role = models.CharField(max_length=50)

#     def __str__(self):
#         return self.full_name


class Loan(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)

    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.book} → {self.member}"