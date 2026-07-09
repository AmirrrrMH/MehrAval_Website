from django import forms
from website.models import User


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ["created_date", "updated_date"]
