from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("newPage", views.newPage, name="newPage"),
    path("create", views.create, name="create"),
    path("edit", views.edit, name="edit"),
    path("editPage/<str:title>", views.showEditPage, name="editPage"),
    path("<str:title>", views.title, name="title")
]
