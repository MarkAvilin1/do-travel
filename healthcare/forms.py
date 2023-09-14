from django import forms

from .models import Hair, Dentist, Plastic, Optic, General


class HairForm(forms.ModelForm):
    class Meta:
        model = Hair
        fields = '__all__'


class DentistForm(forms.ModelForm):
    class Meta:
        model = Dentist
        fields = '__all__'


class PlasticForm(forms.ModelForm):
    class Meta:
        model = Plastic
        fields = '__all__'


class OpticForm(forms.ModelForm):
    class Meta:
        model = Optic
        fields = '__all__'


class GeneralForm(forms.ModelForm):
    class Meta:
        model = General
        fields = '__all__'
