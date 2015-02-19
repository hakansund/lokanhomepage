from django import forms
from .models import Vote


class VoteForm(forms.ModelForm):
    BOOLEAN_CHOICES = (('1', 'Ja'), ('0', 'Nej'))
    positive = forms.ChoiceField(choices=BOOLEAN_CHOICES,
        widget=forms.RadioSelect)

    class Meta:
        model = Vote
        fields = ['positive']