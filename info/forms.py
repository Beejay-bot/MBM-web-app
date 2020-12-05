from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phoneNumber =  forms.CharField(max_length=15, required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4 
    }))