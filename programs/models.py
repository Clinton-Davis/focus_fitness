from django.db import models
from django.urls import reverse
from memberships.models import Membership
from ckeditor.fields import RichTextField


class Program(models.Model):

    slug = models.SlugField()
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True)
    thumbnail = models.ImageField()
    allowed_memberships = models.ManyToManyField(Membership)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('programs:detail', kwargs={'slug': self.slug})

    @property
    def workouts(self):
        return self.workout_set.all().order_by('position')


class Workout(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=200)
    Program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    position = models.IntegerField()
    video_url = models.CharField(max_length=200)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('programs:workout-detail', kwargs={'program_slug': self.Program.slug,
                                                          'workout_slug': self.slug})
