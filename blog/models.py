from django.db import models
from profiles.models import UserProfile


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
    #                            null=True, blank=True, related_name='')

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    """To be able to comment on a blog"""
    # user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
    #                            null=True, blank=True, related_name='user')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class BlogView(models.Model):
    """Keeps track of unike views """
    # user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
    #                            null=True, blank=True, related_name='user')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    """To keep track of all the likes """
    # user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
    #                            null=True, blank=True, related_name='user')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
