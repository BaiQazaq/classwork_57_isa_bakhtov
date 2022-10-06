from django import forms
# from django.forms import widgets
from django.core.exceptions import ValidationError

from webapp.models import Article, Tag


class ArticleForm(forms.ModelForm):
    # title = forms.CharField(max_length=200, required=True, label='Заголовок')
    # author = forms.CharField(max_length=10, required=True, label='Автор')
    # text = forms.CharField(
    #     max_length=2000,
    #     required=True,
    #     label='Текст',
    #     widget=widgets.Textarea
    #     )
    #tags = forms.ModelMultipleChoiceField(required=False, label='Тэги', queryset=Tag.objects.all())
    
    class Meta:
        model = Article
        fields = ('title', 'author', 'text', 'status', 'tags')
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длинее 2x символов')
        return title