from django.contrib import admin
from .models import Author, Publisher, Category, Book, Member, Staff, Loan


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


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "email")
    search_fields = ("full_name", "email")


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "role")


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ("id", "book", "member", "issue_date", "due_date", "return_date")
    list_filter = ("issue_date",)