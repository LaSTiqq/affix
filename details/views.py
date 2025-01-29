from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from smtplib import SMTPException
from .forms import ContactForm
from .utils import restricted_found


def send(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            if any(restricted_found(form.cleaned_data[field]) for field in ['name', 'subject', 'content']):
                messages.warning(
                    request, "Jūs ievadījāt kaut ko neatļautu! Mēģiniet vēlreiz.")
                return redirect('/#contact_us')
            html_content = render_to_string('email.html', {
                'name': form.cleaned_data['name'],
                'sender': form.cleaned_data['sender'],
                'content': form.cleaned_data['content']
            })
            text_content = strip_tags(html_content)
            try:
                email = EmailMultiAlternatives(
                    form.cleaned_data['subject'],
                    text_content,
                    settings.EMAIL_HOST_USER,
                    ['affixsia@inbox.lv']
                )
                email.attach_alternative(html_content, 'text/html')
                email.send()
                messages.success(request, "Vēstule nosūtīta!")
                return redirect('/#contact_us')
            except SMTPException:
                messages.warning(
                    request, "Radās kļūda! Mēģiniet vēlreiz.")
                return redirect('/#contact_us')
        else:
            messages.warning(
                request, "Captcha nebija izieta! Mēģiniet vēlreiz.")
            return redirect('/#contact_us')
    else:
        form = ContactForm()
    return render(request, 'index.html', {"form": form})
