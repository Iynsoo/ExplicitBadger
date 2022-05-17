from django import forms
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Passwords must match.")
        return data

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class EditAccountForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_admin = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_instructor = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_ta = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'is_admin', 'is_instructor', 'is_ta')