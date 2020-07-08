from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import reverse, render
from django.views import generic
from .forms import ContactForm


def index(request):
    return render(request, "home/index.html")


def about(request):
    return render(request, "home/about.html")


# class ContactView(generic.FormView):
#     form_class = ContactForm
#     template_name = "contact.html"

#     def get_success_url(self):
#         return reverse("contact")

#     """" Getting clean data from the form and creating
#         a message to get sent to default email"""

#     def form_valid(self, form):
#         messages.success(self.request,
#                          "Thank you for getting in touch with us. We have received your message.")
#         name = form.cleaned_data.get('name')
#         email = form.cleaned_data.get('email')
#         message = form.cleaned_data.get('message')

#         full_message = f"""
#         Received message below from {name}, {email}
#         ___________________________
#         {message}

#         """
#         send_mail(
#             subject="Message from Focus contact form",
#             message=full_message,
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[settings.NOTIFY_EMAIL]
#         )
#         return super(ContactView, self).form_invalid(form)
