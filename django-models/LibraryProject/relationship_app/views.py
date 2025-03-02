from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Book, Library
from django.views.generic import DetailView


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after registration
            return redirect("home")  # Change 'home' to your desired redirect URL
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

