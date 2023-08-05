from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from smtplib import SMTPException
from .forms import ContactForm
import re


def restricted_found(text):
    url_pattern = r"(?:http[s]?://|www\.)[^\s/$.?#].[^\s]*"
    russian_pattern = r"[а-яА-ЯёЁ]"
    restricted_keywords = ["WhatsApp", "whatsapp", "Telegram", "telegram", "tg",
                           "Discord", "discord", "Viber", "viber", "icq", "ICQ",
                           "Skype", "skype", "+7(977)", "+7 (977)", "+7977", "+7 977",
                           "rub", "RUB", "Bonus", "bonus", "Free", "free", "Gift", "gift",
                           "Order now", "order now", "Spam", "spam", "Website", "website",
                           "Visit our", "visit our", "Earn", "earn"]

    has_link = bool(re.search(url_pattern, text))
    has_russian = bool(re.search(russian_pattern, text))
    has_restricted_keyword = any(
        keyword in text for keyword in restricted_keywords)

    return has_link or has_russian or has_restricted_keyword


def send(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            body = {
                'name': form.cleaned_data['name'],
                'sender': form.cleaned_data['sender'],
                'content': form.cleaned_data['content'],
            }
            if restricted_found(body['content']):
                messages.warning(
                    request, "Jūs ievadījāt kaut ko aizliegtu! Ziņa netika nosūtīta")
                return redirect('/#contact_us')
            html_content = render_to_string('email.html', {
                                            'name': body['name'], 'sender': body['sender'], 'content': body['content']})
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
                messages.success(request, 'Vēstule nosūtīta')
                return redirect('/#contact_us')
            except SMTPException:
                messages.error(
                    request, 'Kaut kas nav izdevies, lūdzu, mēģiniet vēlreiz')
                return redirect('/#contact_us')
        else:
            messages.warning(
                request, 'Captcha nebija izieta, lūdzu, mēģiniet vēlreiz')
            return redirect('/#contact_us')
    else:
        form = ContactForm()
    return render(request, 'index.html', {"form": form})
