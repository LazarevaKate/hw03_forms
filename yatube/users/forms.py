from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model

from django.forms import Textarea, Select

from posts.models import Contact

from django import forms

User = get_user_model()


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'body')


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
