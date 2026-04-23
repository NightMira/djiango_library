from django.contrib import admin
from .models import Author, Publisher, Category, Book, Loan, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "full_name", "email", "role", "phone", "date_reg")
    search_fields = ("username", "full_name", "email")
    list_filter = ("role",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name")
    search_fields = ("full_name",)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("isbn", "title", "author", "available", "copies")
    search_fields = ("title", "isbn")
    list_filter = ("category", "author")


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ("id", "book", "user", "issue_date", "due_date", "return_date")
    list_filter = ("issue_date",)