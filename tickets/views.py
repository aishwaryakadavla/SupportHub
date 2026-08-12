from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import TicketForm
from .models import Ticket


@login_required
def create_ticket(request):

    if request.method == "POST":
        form = TicketForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("ticket_list")

    else:
        form = TicketForm()

    return render(
        request,
        "create_ticket.html",
        {"form": form}
    )


@login_required
def ticket_list(request):

    tickets = Ticket.objects.all().order_by("-created_at")

    return render(
        request,
        "ticket_list.html",
        {"tickets": tickets}
    )


@login_required
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
        {"form": form, "ticket": ticket}
    )


@login_required
def delete_ticket(request, ticket_id):

    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == "POST":
        ticket.delete()
        return redirect("ticket_list")

    return render(
        request,
        "delete_ticket.html",
        {"ticket": ticket}
    )
