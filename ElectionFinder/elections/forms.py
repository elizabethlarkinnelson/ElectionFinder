from django import forms

class ElectionForm(forms.Form):
    state = forms.CharField(label='state', max_length=2)
    city = forms.CharField(label='city', max_length=50)