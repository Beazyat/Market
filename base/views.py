from django.shortcuts import render, redirect

from item.models import Category, Item
from .forms import SignupForm
# Create your views here.


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    context = {
        'items': items,
        'categories': categories,
    }
    return render(request, './index.html', context)


def signup(request):
    """
    This function handles the sign up form.

    Parameters:
    request (HttpRequest): The incoming request.

    Returns:
    HttpResponse: The response to the request.
    """
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("/login/")
    else:
        form = SignupForm()

    context = {
        "form": form,
    }
    return render(request, "signup.html", context)