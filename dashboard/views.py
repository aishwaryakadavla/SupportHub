from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket


def home(request):
    return render(request, "home.html")


@login_required
def dashboard_view(request):
    open_tickets = Ticket.objects.filter(status="Open").count()
    in_progress_tickets = Ticket.objects.filter(status="In Progress").count()
    closed_tickets = Ticket.objects.filter(status="Closed").count()

    recent_tickets = Ticket.objects.all().order_by("-created_at")[:3]

    context = {
        "open_tickets": open_tickets,
        "in_progress_tickets": in_progress_tickets,
        "closed_tickets": closed_tickets,
        "recent_tickets": recent_tickets,
    }

    return render(request, "dashboard.html", context)
