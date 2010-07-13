from django.db import models
from tickets.signals import *

class TicketType(models.Model):
    """a category or type of ticket"""
    name = models.CharField(blank=True, max_length=100)
    price = models.FloatField()
    limit = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s ($%.2f)' % (self.name,self.price)

class TicketedEvent(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start = models.DateTimeField(blank=True,null=True)
    slug = models.SlugField()
    ticket_quantity = models.IntegerField(default=0)
    ticket_types = models.ManyToManyField(TicketType)
    default_ticket_type = models.ForeignKey(TicketType,related_name="default_type",null=True,blank=True)
    purchase_limit = models.IntegerField(default=4)
    attendee_required = models.BooleanField(default=True,help_text="Whether to collect attendee name for every ticket")
    
    def __unicode__(self):
        return self.slug
    
    def tickets_available(self):
        return max(self.ticket_quantity - self.tickets.count(),0)
    
    def get_absolute_url():
        return "/tickets/" + self.slug

class TicketPurchase(models.Model):
    date = models.DateField(auto_now_add=True,editable=False)
    amount = models.FloatField()
    email = models.EmailField(default='',verbose_name="email")
    name = models.CharField(max_length=100)
    status = models.CharField(default='pending',max_length=20)
    
    def __unicode__(self):
        return "%s (%s)" % (self.name, self.status)
        
    def paid(self):
        return "completed" in self.status 
    
    def invoice(self):
        return self.id
    
    
        
class Ticket(models.Model):
    """a ticket"""
    event = models.ForeignKey(TicketedEvent,related_name="tickets")
    ticket_type = models.ForeignKey(TicketType)
    purchase = models.ForeignKey(TicketPurchase,related_name="tickets")
    attendee = models.CharField(blank=True,max_length=100)
    
    def __unicode__(self):
        return self.attendee or self.purchase.name
        
    def paid(self):
        return self.purchase.paid()

        