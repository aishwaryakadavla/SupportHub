from django.db import models

# Create your models here.

from django.db import models


class Ticket(models.Model):

    CATEGORY_CHOICES = [
        ("Hardware", "Hardware"),
        ("Software", "Software"),
        ("Network", "Network"),
        ("Other", "Other"),
    ]

    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    STATUS_CHOICES = [
        ("Open", "Open"),
        ("In Progress", "In Progress"),
        ("Closed", "Closed"),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Open"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title