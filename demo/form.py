from django import forms
from turtle import textinput
class CustomerDetails(forms.Form):
    username=forms.CharField( label="usename",widget=forms.TextInput(),required=True)
    number=forms.IntegerField(label="number",widget=forms.TextInput())
    password=forms.CharField(label="password",widget=forms.PasswordInput)