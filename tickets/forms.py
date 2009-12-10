from django import forms
from tickets.models import *

class TicketPurchaseForm(forms.ModelForm):
    class Meta:
        model = TicketPurchase
        fields = ['name','email']
        
class TicketForm(forms.Form):
    attendee = forms.CharField(required=False,label="Attendee Name")
    ticket_type = forms.ModelChoiceField(queryset=None,required=False)
    qty = forms.IntegerField()
    
    def __init__(self,type_qs=None,**kwargs):
        super(TicketForm,self).__init__(**kwargs)
        self.fields['ticket_type'].queryset = type_qs
    
    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['attendee'] and not cleaned_data['ticket_type']:
            raise forms.ValidationError ("A ticket type must be selected for each attendee")
        return cleaned_data
