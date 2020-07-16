from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

import stripe


MEMBERSHIP_CHOICES = (
    ('Free', 'free'),
    ('Professional', 'pro')
)


class Membership(models.Model):

    slug = models.SlugField()
    membership = models.CharField(
        choices=MEMBERSHIP_CHOICES,
        default='Free',
        max_length=30)
    price = models.IntegerField(default=20)
    stripe_plan_id = models.CharField(max_length=50)

    def __str__(self):
        return self.membership_type


def post_save_usermembership_create(sendr, instance, created, *args, **kwargs):
    """Using a Post_save signal to creates the user membership """
    if created:
        UserMembership.objects.get_or_create(user=instance)
    user_membership, created = UserMembership.objects.get_or_create(
        user=instance)

    if user_membership.stripe_customer_id is None or user_membership.stripe_customer_id == '':
        new_customer_id = stripe.Customer.create(email=instance.email)
        user_membership.stripe_customer_id = new_customer_id['id']
        user_membership.save()


post_save.connect(post_save_usermembership_create,
                  sender=settings.AUTH_USER_MODEL)


class UserMembership(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50)
    membership = models.ForeignKey(
        Membership, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username


class Subscription(models.Model):
    user_memdership = models.ForeignKey(
        UserMembership, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_memdership.user.username
