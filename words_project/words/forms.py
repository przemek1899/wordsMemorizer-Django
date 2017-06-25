# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import HiddenInput

from models import Expression, Group, Language


# class UserForm(forms.ModelForm):
#
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta:
#         model = User
#         fields = ('username', 'email')
PASSWORD_LENGTH = 5


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Hasło',
                                help_text='Hasło musi zawierać co najmniej 5 znaków')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Powtórz hasło')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2 or len(password1) < PASSWORD_LENGTH:
            raise ValidationError('password2')
        return password2

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        # self.fields['password1'].widget.attrs.update({'data-parsley-minlength': PASSWORD_LENGTH})
        # self.fields['password2'].widget.attrs.update({'data-parsley-minlength': PASSWORD_LENGTH,
        #                                               'data-parsley-equalto': '#id_dir_usr-password1'})
        # set_attrs(self, self.fields, 'class', 'elem-required')
        # set_attrs(self, self.fields, 'data-parsley-required', "true")
        # set_attrs(self, self.fields, 'data-parsley', 'true')
        # capitalize_fields = ['first_name', 'last_name']
        # set_attrs(self, capitalize_fields, 'data-capitalize', 'true')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save()
        # user.email = self.cleaned_data['email']
        # user.first_name = self.cleaned_data['first_name']
        # user.last_name = self.cleaned_data['last_name']
        # user.username = generate_username(user.first_name, user.last_name)

        if commit:
            user.save()
        return user


class ExpressionForm(forms.ModelForm):

    class Meta:
        model = Expression
        exclude = ('creation_date', )

    def __init__(self, *args, **kwargs):
        user = None
        if 'user' in kwargs:
            user = kwargs.pop('user')
        super(ExpressionForm, self).__init__(*args, **kwargs)
        self.fields['groups'].queryset = Group.objects.filter(user=user)


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        # fields = '__all__'
        exclude = ('user', )

    def __init__(self, *args, **kwargs):
        user = None
        if 'user' in kwargs:
            user = kwargs.pop('user')
        super(GroupForm, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = Group.objects.filter(user=user)
        self.fields['parent'].required = False
        self.fields['language'].queryset = Language.objects.all()


class ExpressionGroupForm(forms.ModelForm):

    class Meta:
        model = Expression
        exclude = ('creation_date', )
    # group = forms.ModelChoiceField(widget=HiddenInput(), disabled=True)

    def __init__(self, *args, **kwargs):
        group = kwargs.pop('group') if 'group' in kwargs else None
        super(ExpressionGroupForm, self).__init__(*args, **kwargs)
        if group:
            self.fields['groups'].disabled = True
            self.fields['groups'].widget = HiddenInput()
            self.fields['groups'].initial = group
