from celery import shared_task
from django.core.mail import send_mail

from .models import Order

@shared_task
def order_created(order_id):
    # task to send an email notification when the order is successfully created
    order = Order.objects.get(id=order_id)
    subject = f'Order Number {order.id}'
    message = f'Dear {order.first_name} \n\n You have successfully placed an order\
         Your order id is {order.id}'
    mail_sent = send_mail(subject,
                          message,
                          'snipherblog@gmail.com',
                          [order.email]
                          )
    return mail_sent