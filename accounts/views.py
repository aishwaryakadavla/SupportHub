from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def login_view(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(
                request,
                "Login successful."
            )

            return redirect("dashboard")

        messages.error(
            request,
            "Invalid email or password."
        )

        return redirect("login")

    return render(request, "login.html")


def register_view(request):

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:

            messages.error(
                request,
                "Passwords do not match."
            )

            return redirect("register")

        if User.objects.filter(username=email).exists():

            messages.error(
                request,
                "An account with this email already exists."
            )

            return redirect("register")

        User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=full_name
        )

        messages.success(
            request,
            "Registration successful. Please log in."
        )

        return redirect("login")

    return render(request, "register.html")


def logout_view(request):

    logout(request)

    messages.success(
        request,
        "You have been logged out successfully."
    )

    return redirect("login")
