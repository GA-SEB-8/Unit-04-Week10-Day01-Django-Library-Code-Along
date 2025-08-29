from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
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
            messages.success(request, "Author created.")
            return redirect("author_detail", pk=author.pk)
    else:
        form = AuthorForm()
    return render(request, "authors/author_form.html", {"form": form, "mode": "Create"})

def author_update(request, pk):
    author = Author.objects.get(pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save()
            messages.success(request, "Author updated.")
            return redirect("author_detail", pk=author.pk)
    else:
        form = AuthorForm(instance=author)
    return render(request, "authors/author_form.html", {"form": form, "mode": "Update"})

def author_delete(request, pk):
    author = Author.objects.get(pk=pk)
    if request.method == "POST":
        author.delete()
        messages.success(request, "Author deleted.")
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
    # ordering = ["last_name", "first_name"]  # optional (already in Meta)


class AuthorDetailView(DetailView):
    model = Author
    template_name = "authors/author_detail.html"
    context_object_name = "author"
    # pk_url_kwarg = "pk"  # default


class AuthorCreateView(SuccessMessageMixin, CreateView):
    model = Author
    form_class = AuthorForm
    template_name = "authors/author_form.html"
    success_message = "Author created."

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["mode"] = "Create"
        return ctx

    def get_success_url(self):
        return reverse("author_detail", kwargs={"pk": self.object.pk})


class AuthorUpdateView(SuccessMessageMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = "authors/author_form.html"
    success_message = "Author updated."

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["mode"] = "Update"
        return ctx

    def get_success_url(self):
        return reverse("author_detail", kwargs={"pk": self.object.pk})


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = "authors/author_confirm_delete.html"
    success_url = reverse_lazy("author_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Author deleted.")
        return super().delete(request, *args, **kwargs)
