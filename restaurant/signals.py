from django.dispatch import Signal
from django.dispatch import receiver
from .models import OrderItem
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
order_items_created = Signal()

@receiver(order_items_created)
def handle_order_items_created(sender, order, **kwargs):
    orderItems = OrderItem.objects.filter(order=order)
    if not orderItems.exists():
        return

    manager_users = set()
    for orderItem in orderItems:
        manager = orderItem.item.restaurant.user
        manager_users.add(manager)

    channel_layer = get_channel_layer()
    for user in manager_users:
        group_name = f"user_{user.id}"
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                'type': 'order_notification',
                'message': f'New Order #{order.id} has been placed for your restaurant.'
            }
        )






