"""
URL configuration for riminder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from app.views import note_list, note_detail, create_note, edit_note, delete_note, reminder_list, reminder_detail, create_reminder, edit_reminder, delete_reminder, base, signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base, name='base'),
    path('note/', note_list, name='note_list'),
    path('note/<int:note_id>/', note_detail, name='note_detail'),
    path('note/create/', create_note, name='create_note'),
    path('note/<int:note_id>/edit/', edit_note, name='edit_note'),
    path('note/<int:note_id>/delete/', delete_note, name='delete_note'),
    path('reminder/', reminder_list, name='reminder_list'),
    path('reminder/<int:reminder_id>/', reminder_detail, name='reminder_detail'),
    path('reminder/create/', create_reminder, name='create_reminder'),
    path('reminder/<int:reminder_id>/edit/', edit_reminder, name='edit_reminder'),
    path('reminder/<int:reminder_id>/delete/', delete_reminder, name='delete_note'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
]


