from django import forms
from django.conf import settings
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.Form):
    name = forms.CharField(label='Vārds', widget=forms.TextInput(attrs={
        'class': 'form-control bg-transparent ms-auto mt-2', 'placeholder': 'Vārds', 'autocomplete': 'off', 'maxlength': '10'}),
        min_length=5)
    sender = forms.EmailField(label='E-pasts', widget=forms.EmailInput(attrs={
        'class': 'form-control bg-transparent ms-auto mt-2', 'placeholder': 'E-pasts', 'autocomplete': 'off'}))
    subject = forms.CharField(label='Temats', widget=forms.TextInput(attrs={
        'class': 'form-control bg-transparent ms-auto mt-2', 'placeholder': 'Temats', 'autocomplete': 'off', 'maxlength': '25'}),
        min_length=5)
    content = forms.CharField(label='Teksts', widget=forms.Textarea(attrs={
        'class': 'form-control bg-transparent me-auto ms-md-2 mt-2 pt-3', 'placeholder': 'Teksts', 'autocomplete': 'off', 'rows': 5}),
        min_length=50)
    captcha = ReCaptchaField(
        label='Captcha',
        widget=ReCaptchaV2Checkbox(
            attrs={
                'style': 'display: flex; justify-content: center; margin-top: 0.5rem;',
                'data-sitekey': settings.RECAPTCHA_PUBLIC_KEY,
                'data-callback': 'enable',
                'data-expired-callback': 'disable',
            },
            api_params={
                'hl': 'lv',
            },
        ),
    )
