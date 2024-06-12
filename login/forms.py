from django.db import models  
from django.forms import fields  
from .models import UserCredential  
from django import forms  
  
  
class ImageForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = UserCredential  
        # It includes all the fields of model  
        fields = ['name','img']  