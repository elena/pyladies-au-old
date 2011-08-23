from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from apps.newsletter.models import Subscription

class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription


        
        
        
