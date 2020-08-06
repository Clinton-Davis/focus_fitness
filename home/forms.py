from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'autofocus': True,
        'class': "form-group",
        'placeholder': "Your Name",

    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': "form-group",
        'placeholder': "Your Email"
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': "form-group",
        'rows': "4",
        'cols': "50",
        'placeholder': "Your Message"}))
