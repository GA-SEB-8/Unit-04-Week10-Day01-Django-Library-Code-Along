from django.shortcuts import render, redirect
from .models import Author
from .forms import AuthorForm

def author_list(request):
    authors = Author.objects.all()
    return render(request, "authors/author_list.html", {"authors": authors})

def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, "authors/author_detail.html", {"author": author})

def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect("author_detail", pk=author.pk)
    else:
        form = AuthorForm()
    return render(request, "authors/author_form.html", {"form": form})

def author_update(request, pk):
    author = Author.objects.get(pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save()
            return redirect("author_detail", pk=author.pk)
    else:
        form = AuthorForm(instance=author)
    return render(request, "authors/author_form.html", {"form": form})

def author_delete(request, pk):
    author = Author.objects.get(pk=pk)
    if request.method == "POST":
        author.delete()
        return redirect("author_list")
    return render(request, "authors/author_confirm_delete.html", {"author": author})




# authors/views.py
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Author
from .forms import AuthorForm


class AuthorListView(ListView):
    model = Author
    template_name = "authors/author_list.html"
    context_object_name = "authors"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "authors/author_detail.html"
    context_object_name = "author"


class AuthorCreateView(SuccessMessageMixin, CreateView):
    model = Author
    form_class = AuthorForm
    template_name = "authors/author_form.html"


    def get_success_url(self):
        return reverse("author_detail", kwargs={"pk": self.object.pk})


class AuthorUpdateView(SuccessMessageMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = "authors/author_form.html"

    def get_success_url(self):
        return reverse("author_detail", kwargs={"pk": self.object.pk})


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = "authors/author_confirm_delete.html"
    success_url = reverse_lazy("author_list")

