# hook up 
from paypal.standard.ipn.signals import payment_was_successful,payment_was_flagged

def payment_success(sender, **kwargs):
    # seems you have to have the import inside the signal handler
    from tickets.models import *
    purchase = TicketPurchase.objects.get(pk=int(sender.invoice))
    purchase.status = sender.payment_status.lower() + " paypal"
    purchase.save()


payment_was_successful.connect(payment_success)
# @@ what to do with payment was flagged?
