from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u'用户名',
        error_messages={'required':u'用户名必须有'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u'用户名',
            }
        ),
        max_length=30,
    )

    email = forms.EmailField(
        required=True,
        label=u'电子邮箱',
        error_messages={'required':u'邮箱是必填项'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u'电子邮箱',
            }
        ),
    )

    content = forms.CharField(
        required=True,
        label=u'内容',
        error_messages={'required':u'你想反馈什么'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u'内容',
            }
        ),
        max_length=300,
    )

    username.widget.attrs.update({'style': 'border-style: groove'})
    email.widget.attrs.update({'style': 'width: 650px; height: 52px; border-style: groove'})
    content.widget.attrs.update({'style': 'border-style: groove'})