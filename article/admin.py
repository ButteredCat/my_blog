from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['category']}),
        (None, {'fields': ['content']}),
        (None, {'fields': ['is_draft']}),
    ]
    list_display = (
        'title', 'category',
        'author', 'date_time',
        'last_updated_by', 'last_updated_in',
        'is_draft'
    )
    list_filter = ['date_time']
    list_editable = ['is_draft']
    search_fields = ['title', 'content', 'category']
    data_hierarchy = 'date_time'

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.author = obj.last_updated_by = request.user
        if change:
            obj.last_updated_by = request.user
        obj.save()

class StackedItemInline(admin.StackedInline):
    classes = ['grp-collapse grp-open']
    inline_classes = ['grp-collapse grp-open']


admin.site.register(Article, ArticleAdmin)
