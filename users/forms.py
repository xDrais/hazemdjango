from django import forms
from users.models import Person


class LoginForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=['username','passowrd']
    passowrd = forms.CharField(label='password',widget=forms.Textarea()
    )