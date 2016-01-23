# -*- coding:utf-8 -*-
from django import forms

from pagedown.widgets import AdminPagedownWidget

from .models import Article, Category


class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget(), required=False,
        label='')

    class Meta:
        model = Article 
        fields = '__all__' # Or a list of the fields you want to include in your form

