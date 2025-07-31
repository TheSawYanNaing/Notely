from . import views 
from django.urls import path 

app_name = "notes"

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("create", views.create, name="create"),
    path("note", views.note, name="note"),
    path("note/<str:category>", views.category, name="category"),
    path("note/<str:category>/<str:title>", views.content, name="content"),
    path("edit/<str:category>/<str:title>", views.edit, name="edit"),
    path("delete/<str:category>/<str:title>", views.delete, name="delete")
]