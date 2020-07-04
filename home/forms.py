from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-group aw", 'placeholder': "Your Name"
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': "form-group aw", 'placeholder': "Your Email"
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': "form-group aw", 'rows': "4", 'cols': "50", 'placeholder': "Your Message"}))
