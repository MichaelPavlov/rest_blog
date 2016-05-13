from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import UserLoginForm, UserRegisterForm


def login_view(request):
    title = "Login"
    next_page = request.GET.get("next")
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if next_page:
            return redirect(next_page)
        return redirect("/")
    context = {
        "form": form,
        "title": title,
    }
    return render(request, "form.html", context)


def register_view(request):
    title = "Register"
    next_page = request.GET.get("next")
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        new_user = authenticate(username=user.username, password=password)
        user.save()
        login(request, new_user)
        if next_page:
            return redirect(next_page)
        return redirect("/")
    context = {
        "form": form,
        "title": title,
    }
    return render(request, "form.html", context)


def logout_view(request):
    logout(request)
    return render(request, "form.html", {})
