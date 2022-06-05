from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("newPage", views.newPage, name="newPage"),
    path("create", views.create, name="create"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("<str:title>", views.title, name="title")
]
