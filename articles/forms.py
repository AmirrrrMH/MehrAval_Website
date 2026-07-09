from django import forms
from .models import Viewpoint


class ViewpointForm(forms.ModelForm):
    class Meta:
        model = Viewpoint
        exclude = ['created_at', 'article_page']
