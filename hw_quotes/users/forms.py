from django import forms
from django.contrib.auth.models import User
from .models import Author, Quote
from django.forms import CharField, TextInput, Textarea, ModelChoiceField, Select


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class AuthorForm(forms.ModelForm):
    fullname = CharField(max_length=50, min_length=2, required=True,
                         widget=TextInput(attrs={"class": "form-control", "id": "exampleInputEmail1"}))
    description = CharField(widget=Textarea)

    class Meta:
        model = Author
        fields = ['fullname', 'description']


class QuoteForm(forms.ModelForm):
    quote = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))

    class Meta:
        model = Quote
        fields = ['quote', 'author']

    def __init__(self, *args, **kwargs):
        super(QuoteForm, self).__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.all()