from django import forms
from django.conf import settings
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.Form):
    name = forms.CharField(label='Vārds', widget=forms.TextInput(attrs={
                           'class': 'form-control bg-transparent ms-auto mt-2', 'placeholder': 'Vārds', 'autocomplete': 'off', 'required': True}))
    sender = forms.EmailField(label='E-pasts', widget=forms.EmailInput(
        attrs={'class': 'form-control bg-transparent ms-auto mt-2', 'placeholder': 'E-pasts', 'autocomplete': 'off', 'required': True}))
    subject = forms.CharField(label='Temats', widget=forms.TextInput(
        attrs={'class': 'form-control bg-transparent ms-auto mt-2', 'placeholder': 'Temats', 'autocomplete': 'off', 'required': True}))
    content = forms.CharField(label='Teksts', widget=forms.Textarea(
        attrs={'class': 'form-control bg-transparent me-auto ms-md-2 mt-2 pt-3', 'rows': 5, 'placeholder': 'Teksts', 'autocomplete': 'off', 'required': True}))
    captcha = ReCaptchaField(
        label='Captcha',
        widget=ReCaptchaV2Checkbox(
            attrs={
                'style': 'display: flex; justify-content: center; margin-top: 0.5rem;',
                'data-sitekey': settings.RECAPTCHA_PUBLIC_KEY,
            },
            api_params={
                'hl': 'lv',
            },
        ),
    )
