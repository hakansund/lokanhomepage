from django import forms


class SubscriptionForm(forms.Form):

    activities = forms.BooleanField(label='Aktiviteter', required=False)

    funding = forms.BooleanField(label='Projektbidrag', required=False)
