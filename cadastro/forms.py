from django import forms

class Cadastro(forms.Form):
    email = forms.CharField(label='email', max_length=100, required=True)
    senha = forms.CharField(label="senha", max_length=20, required=False)
    nascimento = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))