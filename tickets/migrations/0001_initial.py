
from south.db import db
from django.db import models
from tickets.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'TicketType'
        db.create_table('tickets_tickettype', (
            ('id', orm['tickets.TicketType:id']),
            ('name', orm['tickets.TicketType:name']),
            ('price', orm['tickets.TicketType:price']),
            ('limit', orm['tickets.TicketType:limit']),
        ))
        db.send_create_signal('tickets', ['TicketType'])
        
        # Adding model 'TicketPurchase'
        db.create_table('tickets_ticketpurchase', (
            ('id', orm['tickets.TicketPurchase:id']),
            ('date', orm['tickets.TicketPurchase:date']),
            ('amount', orm['tickets.TicketPurchase:amount']),
            ('email', orm['tickets.TicketPurchase:email']),
            ('name', orm['tickets.TicketPurchase:name']),
            ('status', orm['tickets.TicketPurchase:status']),
        ))
        db.send_create_signal('tickets', ['TicketPurchase'])
        
        # Adding model 'TicketedEvent'
        db.create_table('tickets_ticketedevent', (
            ('id', orm['tickets.TicketedEvent:id']),
            ('name', orm['tickets.TicketedEvent:name']),
            ('description', orm['tickets.TicketedEvent:description']),
            ('start', orm['tickets.TicketedEvent:start']),
            ('slug', orm['tickets.TicketedEvent:slug']),
            ('ticket_quantity', orm['tickets.TicketedEvent:ticket_quantity']),
            ('default_ticket_type', orm['tickets.TicketedEvent:default_ticket_type']),
            ('purchase_limit', orm['tickets.TicketedEvent:purchase_limit']),
            ('attendee_required', orm['tickets.TicketedEvent:attendee_required']),
        ))
        db.send_create_signal('tickets', ['TicketedEvent'])
        
        # Adding model 'Ticket'
        db.create_table('tickets_ticket', (
            ('id', orm['tickets.Ticket:id']),
            ('event', orm['tickets.Ticket:event']),
            ('ticket_type', orm['tickets.Ticket:ticket_type']),
            ('purchase', orm['tickets.Ticket:purchase']),
            ('attendee', orm['tickets.Ticket:attendee']),
        ))
        db.send_create_signal('tickets', ['Ticket'])
        
        # Adding ManyToManyField 'TicketedEvent.ticket_types'
        db.create_table('tickets_ticketedevent_ticket_types', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ticketedevent', models.ForeignKey(orm.TicketedEvent, null=False)),
            ('tickettype', models.ForeignKey(orm.TicketType, null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'TicketType'
        db.delete_table('tickets_tickettype')
        
        # Deleting model 'TicketPurchase'
        db.delete_table('tickets_ticketpurchase')
        
        # Deleting model 'TicketedEvent'
        db.delete_table('tickets_ticketedevent')
        
        # Deleting model 'Ticket'
        db.delete_table('tickets_ticket')
        
        # Dropping ManyToManyField 'TicketedEvent.ticket_types'
        db.delete_table('tickets_ticketedevent_ticket_types')
        
    
    
    models = {
        'tickets.ticket': {
            'attendee': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tickets'", 'to': "orm['tickets.TicketedEvent']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purchase': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tickets'", 'to': "orm['tickets.TicketPurchase']"}),
            'ticket_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tickets.TicketType']"})
        },
        'tickets.ticketedevent': {
            'attendee_required': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'default_ticket_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'default_type'", 'blank': 'True', 'null': 'True', 'to': "orm['tickets.TicketType']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'purchase_limit': ('django.db.models.fields.IntegerField', [], {'default': '4'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'ticket_quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ticket_types': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tickets.TicketType']"})
        },
        'tickets.ticketpurchase': {
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '20'})
        },
        'tickets.tickettype': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {})
        }
    }
    
    complete_apps = ['tickets']
