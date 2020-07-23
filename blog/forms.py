from django import forms
from .models import Blog, BlogComment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'title',
            'category',
            'content',
            'thumbnail',

        )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Your Blogs Title',
            'content': 'Write your Blog in here',
            'thumbnail': 'Picture',

        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'category':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'mont_r'
            self.fields[field].label = False


class BlogCommentForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'rows': 4
    }))

    class Meta:
        model = BlogComment
        fields = ('content', )
