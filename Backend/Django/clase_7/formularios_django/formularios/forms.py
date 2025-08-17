from django import forms


class MyForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your name', "class": "form-control"}))
    email = forms.EmailField(label='Your email', initial='example@example.com', widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', "class": "form-control"}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'placeholder': 'Enter your message', "class": "form-control"}))



from django import forms

class RegistroForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    edad = forms.IntegerField(min_value=18, max_value=99, required=True)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, required=True)
    confirmar_password = forms.CharField(widget=forms.PasswordInput, required=True)

    # Validación personalizada para un campo
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if any(char.isdigit() for char in nombre):
            raise forms.ValidationError("El nombre no puede contener números.")
        return nombre

    # Validación para todo el formulario
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmar_password = cleaned_data.get("confirmar_password")

        if password != confirmar_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")
