from django import forms


class MyForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email', initial='example@example.com')
    message = forms.CharField(label='Message')