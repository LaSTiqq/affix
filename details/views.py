from django.views.decorators.http import require_POST, require_GET
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
from smtplib import SMTPException
from .forms import ContactForm
from .utils import restricted_found
import re


@require_GET
def home(request):
    form = ContactForm()
    return render(request, 'index.html', {'form': form})


@require_POST
def send_ajax(request):
    form = ContactForm(data=request.POST)
    if form.is_valid():
        if any(restricted_found(form.cleaned_data[field]) for field in ['name', 'subject', 'message']):
            return JsonResponse({
                "status": "warning",
                "message": "Jūs ievadījāt kaut ko aizliegtu! Lūdzu, mēģiniet vēlreiz."
            }, status=400)

        html_content = render_to_string("email.html", {
            'name': form.cleaned_data['name'],
            'email': form.cleaned_data['email'],
            'message': form.cleaned_data['message']
        })
        text_content = re.sub(r"<[^>]+>", "", html_content)

        try:
            email = EmailMultiAlternatives(
                form.cleaned_data['subject'],
                text_content,
                settings.EMAIL_HOST_USER,
                ['affixsia@inbox.lv']
            )
            email.attach_alternative(html_content, "text/html")
            email.send()
            return JsonResponse({
                "status": "success",
                "message": "Vēstule nosūtīta!"
            })
        except SMTPException:
            return JsonResponse({
                "status": "danger",
                "message": "Kaut kas nogāja greizi! Lūdzu, mēģiniet vēlreiz."
            }, status=500)
    else:
        return JsonResponse({
            "status": "warning",
            "message": "Captcha netika izpildīta! Lūdzu, mēģiniet vēlreiz."
        }, status=500)


@require_POST
def accept_cookies(request):
    response = HttpResponse("Cookie Accepted")
    response.set_cookie(
        key="cookie_accepted",
        value="true",
        max_age=31536000,
        secure=True,
        samesite="Lax",
    )
    return response
