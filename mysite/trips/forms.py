from django import forms
from datetime import date
from django.forms.widgets import TextInput
__author__ = 'user'

from trips.models import Post


class ContentForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="content", widget=forms.Textarea)
    photo = forms.URLField(label="Photo Url")
    location = forms.CharField(label="Location")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Post


