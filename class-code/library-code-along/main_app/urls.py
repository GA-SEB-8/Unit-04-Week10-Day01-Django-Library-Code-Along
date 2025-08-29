from django.urls import path
from . import views


urlpatterns = [

    # path("authors/", views.author_list, name="author_list"),
    # path("authors/new/", views.author_create, name="author_create"),
    # path("authors/<int:pk>/", views.author_detail, name="author_detail"),
    # path("authors/<int:pk>/edit/", views.author_update, name="author_update"),
    # path("authors/<int:pk>/delete/", views.author_delete, name="author_delete"),


    # CBV:
    path("authors/", views.AuthorListView.as_view(), name="author_list"),
    path("authors/new/", views.AuthorCreateView.as_view(), name="author_create"),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view(), name="author_detail"),
    path("authors/<int:pk>/edit/", views.AuthorUpdateView.as_view(), name="author_update"),
    path("authors/<int:pk>/delete/", views.AuthorDeleteView.as_view(), name="author_delete"),


]
