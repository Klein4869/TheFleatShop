from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u'用户名',
        error_messages={'required': '请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder': u'用户名',
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label=u'密码',
        error_messages={'required': '请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u'密码'
            }
        ),
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u'邮箱和密码都为必填项')
        else:
            cleaned_data = super(LoginForm, self).clean()


class RegistForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u'用户名',
        error_messages={'required': '必填项'},
        widget=forms.TextInput(
            attrs={
                'placeholder': u'用户名'
            }
        ),
    )

    email = forms.EmailField(
        required=True,
        label=u'电子邮箱',
        error_messages={'required':'邮箱必须合法'},
        widget=forms.EmailInput(
            attrs={
                'placeholder': u'电子邮箱'
            }
        ),
    )

    password = forms.CharField(
        required=True,
        label=u'密码',
        error_messages={'required': '请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u'密码'
            }
        ),
    )

    re_password = forms.CharField(
        required=True,
        label=u'重复密码',
        error_messages={'required': '请再次输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u'重复密码'
            }
        ),
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u'未完全填写信息')
        else:
            cleaned_data = super(RegistForm, self).clean()