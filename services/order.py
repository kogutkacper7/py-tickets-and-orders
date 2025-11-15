import datetime

from django.db.models import QuerySet
from typing import Optional
from db.models import User, Order, Ticket, MovieSession
from django.db import transaction


def create_order(
        tickets: list[dict],
        username: str,
        date: Optional[datetime] = None
) -> Order:
    with transaction.atomic():

        user = User.objects.get(username=username)

        if date:
            order = Order.objects.create(created_at=date, user=user)
        else:
            order = Order.objects.create(user=user)

        for ticket in tickets:
            movie_session = MovieSession.objects.get(
                id=ticket["movie_session"]
            )
            Ticket.objects.create(
                movie_session=movie_session,
                order=order,
                row=ticket["row"],
                seat=ticket["seat"]
            )
        return order


def get_orders(username: str = None) -> QuerySet:
    if username:
        orders = Order.objects.filter(user__username=username)
    else:
        orders = Order.objects.all()

    return orders
