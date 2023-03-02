from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from smtplib import SMTPException
from .forms import ContactForm

def send(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            body = {
                'name': form.cleaned_data['name'],
                'sender': form.cleaned_data['sender'],
                'content': form.cleaned_data['content'],
            }
            html_content = render_to_string('email.html', {
                                            'name': body['name'], 'sender': body['sender'], 'content': body['content']})
            text_content = strip_tags(html_content)
            try:
                email = EmailMultiAlternatives(
                    form.cleaned_data['subject'],
                    text_content,
                    'affixsia@gmail.com',
                    ['affixsia@inbox.lv']
                )
                email.attach_alternative(html_content, 'text/html')
                email.send()
                messages.success(request, 'Vēstule nosūtīta')
                return redirect('/#contact_us')
            except SMTPException:
                messages.error(request, 'Kaut kas nav izdevies, lūdzu, mēģiniet vēlreiz')
                return render(request, 'details/index.html', {"form": form})
            return redirect('/#contact_us')
        else:
            messages.warning(request, 'Captcha nebija nospiesta, lūdzu, mēģiniet vēlreiz')
            return render(request, 'details/index.html', {"form": form})
        return redirect('/#contact_us')
    else:
        form = ContactForm()
    return render(request, 'details/index.html', {"form": form})