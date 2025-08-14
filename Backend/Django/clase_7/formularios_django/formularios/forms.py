from django import forms


class MyForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your name', "class": "form-control"}))
    email = forms.EmailField(label='Your email', initial='example@example.com', widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', "class": "form-control"}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'placeholder': 'Enter your message', "class": "form-control"}))