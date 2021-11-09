from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Cliente


class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = Cliente
        fields = ('username', 'email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super(UpdateProfile, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.save()

class profileForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    direccion = forms.CharField(required=False)
    class Meta:
        model = Cliente
        fields = ['first_name','last_name', 'email','direccion']

class UploadFileForm(forms.Form):
   nombre = forms.CharField(max_length=50)
   archivo = forms.FileField()