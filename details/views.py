from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import ContactForm

def send(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        try:
            form.is_valid()
        except ValidationError:
            messages.danger(request, 'Captcha ir kļūdaina, mēģiniet vēlreiz')
            return redirect('/#contact_us')
        body = {
            'name': form.cleaned_data['name'],
            'sender': form.cleaned_data['sender'],
            'content': form.cleaned_data['content'],
        }
        html_content = render_to_string('email.html', {
                                        'name': body['name'], 'sender': body['sender'], 'content': body['content']})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            form.cleaned_data['subject'],
            text_content,
            'affixsia@gmail.com',
            ['affixsia@inbox.lv']
        )
        email.attach_alternative(html_content, 'text/html')
        email.send()
        if email:
            messages.success(request, 'Vēstule nosūtīta')
            return redirect('/#contact_us')
        else:
            messages.danger(request, 'Kaut kas nav izdevies, mēģiniet vēlreiz')
            return redirect('/#contact_us')
    else:
        form = ContactForm()
    return render(request, 'details/index.html', {"form": form})