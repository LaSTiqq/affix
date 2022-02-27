from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput

class ContactForm(forms.Form):
    name = forms.CharField(label='Vārds', widget=forms.TextInput(attrs={'class': 'center-block', 'placeholder': 'Vārds'}))
    sender = forms.CharField(label='E-pasts', widget=forms.EmailInput(attrs={'class': 'center-block', 'placeholder': 'E-pasts'}))
    subject = forms.CharField(label='Temats', widget=forms.TextInput(attrs={'class': 'center-block', 'placeholder': 'Temats'}))
    content = forms.CharField(label='Teksts', widget=forms.Textarea(attrs={'class': 'center-block', 'rows': 5, 'placeholder': 'Teksts'}))
    captcha = CaptchaField(label='Captcha', widget=CaptchaTextInput(attrs={'class': 'center-block-add', 'placeholder': 'Atbilde'}))