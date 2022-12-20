from django import forms
from newapp.models import Image

class ImageForm(forms.ModelForm):
  class Meta:
    model = Image
    fields = '__all__'
    labels = {'photo':''}