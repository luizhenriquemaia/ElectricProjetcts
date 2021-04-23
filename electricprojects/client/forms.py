from django import forms


class formDataClient(forms.Form):
    treatment = forms.CharField(max_length=30, required=True)
    name = forms.CharField(max_length=300, required=True)
    cnpj = forms.CharField(max_length=14, required=False)
    description = forms.CharField(max_length=300, required=True)
    fone = forms.CharField(max_length=15, required=False)
    email = forms.EmailField(required=False)