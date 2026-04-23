from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book/<str:isbn>/", views.book_detail, name="book_detail"),

    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),

    path("profile/", views.profile, name="profile"),
    path("borrow/<str:isbn>/", views.borrow_book, name="borrow_book"),

    # библиотекарь
    path("librarian/", views.librarian_dashboard, name="librarian_dashboard"),
    path("librarian/issue/", views.issue_book, name="issue_book"),
    path("librarian/return/<int:loan_id>/", views.return_book, name="return_book"),

    path('register/', views.register_view, name='register'),
    path('profile/', views.profile, name='profile'),
]