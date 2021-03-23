from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm

from .models import UserProfile


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('age', 'desc', 'avatar')


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def save(self, commit=True):
        new_user = User.objects.create_user(self.cleaned_data['username'],
                                            self.cleaned_data['email'],
                                            self.cleaned_data['password'])
        if commit:
            new_user.save()
        return new_user
