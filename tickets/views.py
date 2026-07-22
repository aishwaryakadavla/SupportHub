from django.shortcuts import render

# Create your views here.

def create_ticket(request):
    return render(request, "create_ticket.html")

def ticket_list(request):
    return render(request, "ticket_list.html")