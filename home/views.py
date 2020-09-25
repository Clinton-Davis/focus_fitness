from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import reverse, render
from django.views import generic
from django.views.generic import TemplateView
from .forms import ContactForm
from programs.models import Program
from products.models import Product
from blog.models import Blog
from products.models import Category
from memberships.views import get_user_membership


def IndexView(request):
    feature_blog = Blog.objects.filter(featured=True)
    sales_items = Product.objects.filter(sales_items=True)
    programs = Program.objects.all()
    category = Category.objects.all()

    if request.user.is_authenticated:
        current_membership = get_user_membership(request)
        current_membership = str(current_membership.membership)

    else:
        current_membership = False

    context = {
        'feature_blog': feature_blog,
        'sales_items': sales_items,
        'programs': programs,
        'current_membership': current_membership,
        'category': category
    }

    return render(request, "home/index.html", context)


class AboutView(TemplateView):
    template_name = "home/about.html"


class TermsView(TemplateView):
    template_name = "home/terms.html"


class PrivacyView(TemplateView):
    template_name = "home/privacy.html"


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = "home/contact.html"

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        """"Getting clean data from the form and creating
        a message to get sent to default email."""
        messages.success(self.request,
                         "Thank you for getting in touch with us. We have received your message.")
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        full_message = f"""
        Received message below from {name}, {email}
        ___________________________
        {message}

        """
        send_mail(
            subject="Message from Focus contact form",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(ContactView, self).form_invalid(form)
