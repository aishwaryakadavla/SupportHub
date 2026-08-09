from django.shortcuts import render, redirect, get_object_or_404
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


def update_ticket(request, ticket_id):

    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)

        if form.is_valid():
            form.save()
            return redirect("ticket_list")

    else:
        form = TicketForm(instance=ticket)

    return render(
        request,
        "update_ticket.html",
        {"form": form, "ticket": ticket},
    )


def delete_ticket(request, ticket_id):

    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == "POST":
        ticket.delete()
        return redirect("ticket_list")

    return render(
        request,
        "delete_ticket.html",
        {"ticket": ticket},
    )