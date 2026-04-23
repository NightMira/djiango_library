from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from library_app import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('library_app.urls')),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),

    path('', RedirectView.as_view(url='/login/')),
]