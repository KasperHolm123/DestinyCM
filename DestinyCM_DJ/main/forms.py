from configparser import MAX_INTERPOLATION_DEPTH
from socket import fromshare
from django import forms

class AuthenticateAccount(forms.Form):
    URL = forms.CharField(label='url', max_length=1000, required=False)