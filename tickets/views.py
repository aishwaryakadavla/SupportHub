from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import Ticket


def create_ticket(request):

    if request.method == "POST":
        form = TicketForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("ticket_list")

    else:
        form = TicketForm()

    return render(request, "create_ticket.html", {"form": form})


def ticket_list(request):

    tickets = Ticket.objects.all().order_by("-created_at")

    return render(
        request,
        "ticket_list.html",
        {"tickets": tickets},
    )