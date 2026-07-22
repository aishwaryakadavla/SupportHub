from django.urls import path
from . import views

urlpatterns = [
    path("create-ticket/", views.create_ticket, name="create_ticket"),
    path("ticket-list/", views.ticket_list, name="ticket_list"),

]