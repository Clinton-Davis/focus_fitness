from django import forms
from .models import productComment


class ProductCommentForm(forms.ModelForm):

    ratings = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    rating = forms.CharField(required=True, widget=forms.Select(
        choices=ratings, attrs={'class': 'form-control'}), label="Rate Product Out of 5")

    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'rows': 4,
    }), label="Review")

    class Meta:
        model = productComment
        fields = ('content', 'rating',)
