from django import forms

from django.forms import Textarea, Select

from posts.models import Post


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


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
