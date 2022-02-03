from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model

from django.forms import Textarea, Select

from posts.models import Post, Contact

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


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        widgets = {'text': Textarea(attrs={
            'class': 'form-control',
            'cols': '40',
            'rows': '10'}),
            'group': Select(attrs={
                'class': 'form-control'
            })
        }

    def clean_text_clean(self):
        data = self.cleaned_data['text']
        if data == '':
            raise forms.ValidationError('Вставьте текст')
        return data
