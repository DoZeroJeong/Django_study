from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 확인',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username']
        labels = {
            'username': _('닉네임'),
        }

        def clean_password2(self):
            cd = self.clean_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
            return cd['password2']