# -*- coding:utf-8 -*-
from django.contrib import admin

from .forms import ArticleForm
from .models import Article, Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    readonly_fields = ['author', 'date_time', 'last_updated_in',
            'last_updated_by',]
    fieldsets = [
        (u'标题与分类', {'fields': ['title', 'category']}),
        (u'发布', {
            'fields': ['author', 'date_time', 'last_updated_by',
                'last_updated_in', 'is_draft'], 
            'classes': ['collapse']
            }
        ),
        (u'正文', {'fields': ['content']}),
    ]
    list_display = (
        'title', 'category', 
        'author', 'date_time', 
        'is_draft'
    )
    list_filter = ['date_time', 'is_draft']
    list_per_page = 20
    list_editable = ['category', 'is_draft']
    search_fields = ['title', 'content']
    data_hierarchy = 'date_time'

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.author = obj.last_updated_by = request.user
        if change:
            obj.last_updated_by = request.user
        obj.save()


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

