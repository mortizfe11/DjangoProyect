from .models import Member
from django import forms 

class CreateMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('firstname', 'lastname', 'phone',)


class UpdateMemberForm(forms.ModelForm):
    firstname = forms.CharField(required=False)
    lastname = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    
    class Meta:
        model = Member
        fields = ('firstname', 'lastname', 'phone',)
