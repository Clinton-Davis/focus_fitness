from django import forms
from .models import Blog, BlogComment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('__all__')


class BlogCommentForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'rows': 4
    }))

    class Meta:
        model = BlogComment
        fields = ('content', )
