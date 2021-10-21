from django.db import models
from django.forms import ModelForm, fields
from .models import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
