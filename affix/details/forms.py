from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput

class ContactForm(forms.Form):
    name = forms.CharField(label='Vārds', widget=forms.TextInput(attrs={'class': 'd-block ms-auto', 'placeholder': 'Vārds',
																			'onpaste': 'return false;',
																			'ondrop': 'return false;',
																			'autocomplete': 'off'}))
    sender = forms.CharField(label='E-pasts', widget=forms.EmailInput(attrs={'class': 'd-block ms-auto', 'placeholder': 'E-pasts',
																			'onpaste': 'return false;',
																			'ondrop': 'return false;',
																			'autocomplete': 'off'}))
    subject = forms.CharField(label='Temats', widget=forms.TextInput(attrs={'class': 'd-block ms-auto', 
																			'placeholder': 'Temats',
																			'onpaste': 'return false;',
																			'ondrop': 'return false;',
																			'autocomplete': 'off'}))
    content = forms.CharField(label='Teksts', widget=forms.Textarea(attrs={'class': 'mx-auto', 'rows': 5,
																			'placeholder': 'Teksts',
																			'onpaste': 'return false;',
																			'ondrop': 'return false;',
																			'autocomplete': 'off'}))
    captcha = CaptchaField(label='Captcha', widget=CaptchaTextInput(attrs={'class': 'd-block mx-auto', 'placeholder': 'Atbilde (cipars vai skaitlis)'}))