from .models import Member
from django import forms 

class CreateMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('firstname', 'lastname', 'phone', 'joined_date',)
