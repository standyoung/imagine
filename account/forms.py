from django.contrib.auth import authenticate
from account.models import User
from django import forms


class AccountAuthForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = User()
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid login")
