from django import forms
from .models import Tu_Data
from django.utils.translation import ugettext_lazy as _


class TuDataForm(forms.ModelForm):
    class Meta:
        model = Tu_Data
        fields = {'tu_id', 'tu_password', 'first_day', 'second_day', 'apply_text'}
        labels = {
            'tu_id': _('학번'),
            'tu_password': _('비밀번호'),
            'first_day': _('외박 시작일'),
            'second_day': _('외박 종료일'),
            'apply_text': _('외박 사유'),
        }
        widgets = {
            'tu_password': forms.PasswordInput()
        }
