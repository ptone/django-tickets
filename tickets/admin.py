from django.contrib import admin
from tickets.models import *

class TicketInline(admin.TabularInline):
    model = Ticket

class PurchaseAdmin (admin.ModelAdmin):
    list_display = ('invoice','name','date','amount')
    inlines = [TicketInline]

class TicketAdmin (admin.ModelAdmin):
    list_display = ('event','ticket_type','attendee','purchase')
    
admin.site.register(TicketType)
admin.site.register(TicketPurchase,PurchaseAdmin)
admin.site.register(TicketedEvent)
admin.site.register(Ticket, TicketAdmin)