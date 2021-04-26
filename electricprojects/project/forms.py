from django import forms

from client.models import b01Clients, b02Address


class formNewProject(forms.Form):
    client = forms.ModelChoiceField(queryset=b01Clients.objects.all().only('id', 'description'),
        widget=forms.Select(attrs={'onchange': "loadAddressClient(this);"}))
    address = forms.ModelChoiceField(queryset=b02Address.objects.none())
    description = forms.CharField(max_length=250, required=False)
    observation = forms.CharField(max_length=500, required=False,
        widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            if 'client' in self.data:
                client = self.data.get('client')
                self.fields['address'].queryset = b02Address.objects.filter(
                    client_id=client).order_by('id')
        except(ValueError, TypeError):
            pass