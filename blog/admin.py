from blog.models import Category, Post, Tag
from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

    
admin.site.register(Tag, TagAdmin)


class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'publish', 'created', 'updated', 'status', 'views', 'category')
    list_display_links = ('id', 'author', 'title')
    search_fields = ('title', 'body')
    list_filter = ('status', 'created', 'publish', 'author')
    ordering = ('status', 'publish')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    raw_id_fields = ('author',)
    form = PostAdminForm
    save_as = True
    save_on_top = True
    readonly_fields = ('views', 'created', 'updated', 'publish')
    fields = ('author', 'title', 'slug', 'category', 'tags', 'photo', 'body', 'publish', 'created', 'updated', 'status', 'views', )
    list_editable = ('status',)


admin.site.register(Post, PostAdmin)






