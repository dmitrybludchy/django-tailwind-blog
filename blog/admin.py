from blog.models import Category, Post, Tag
from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'publish', 'created', 'updated', 'status', 'views', 'category')
    list_display_links = ('author', 'title')
    search_fields = ('title', 'body')
    list_filter = ('status', 'created', 'publish', 'author', 'tags')
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





