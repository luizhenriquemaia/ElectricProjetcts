from django import forms

from main.models import a10State, a11City, a12District


class formDataClient(forms.Form):
    treatment = forms.CharField(max_length=30, required=True)
    name = forms.CharField(max_length=300, required=True)
    cnpj = forms.CharField(max_length=14, required=False)
    description = forms.CharField(max_length=300, required=True)
    fone = forms.CharField(max_length=15, required=False)
    email = forms.EmailField(required=False)


class formAddress(forms.Form):
    state = forms.ModelChoiceField(queryset=a10State.objects.all(),
        widget=forms.Select(attrs={'onchange': "loadData(this);"}))
    city = forms.ModelChoiceField(queryset=a11City.objects.none(),
        widget=forms.Select(attrs={'onchange': "loadData(this);"}))
    district = forms.ModelChoiceField(queryset=a12District.objects.none(),
        widget=forms.Select(attrs={'onchange': "loadData(this);"}), required=False)
    new_district = forms.CharField(max_length=200, required=False)
    street = forms.CharField(max_length=200, required=True)
    complement = forms.CharField(max_length=300, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            if 'state' in self.data:
                state = self.data.get('state')
                self.fields['city'].queryset = a11City.objects.filter(
                    state_id=state).order_by('description')
            if 'city' in self.data:
                city = self.data.get('city')
                self.fields['district'].queryset = a12District.objects.filter(
                    city_id=city).order_by('description')
        except(ValueError, TypeError):
            pass