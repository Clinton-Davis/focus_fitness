from django.db import models
from profiles.models import User
from django.shortcuts import reverse


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:details', kwargs={'slug': self.slug})

    def get_like_url(self):
        return reverse('blog:like', kwargs={'slug': self.slug})

    @property
    def get_comment_count(self):
        return self.blogcomment_set.all().count()

    @property
    def get_view_count(self):
        return self.blogview_set.all().count()

    @property
    def get_like_count(self):
        return self.like_set.all().count()

    @property
    def blogcomments(self):
        return self.blogcomment_set.all()


class BlogComment(models.Model):
    """To be able to comment on a blog"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class BlogView(models.Model):
    """Keeps track of unike views """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    """To keep track of all the likes """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
