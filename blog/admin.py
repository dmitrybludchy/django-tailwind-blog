from blog.models import Category, Post, Tag
from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

    
admin.site.register(Tag, TagAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'publish', 'created', 'updated', 'status', 'views', 'category')
    list_display_links = ('id', 'author', 'title')
    search_fields = ('title', 'body')
    list_filter = ('status', 'created', 'publish', 'author')
    ordering = ('status', 'publish')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    raw_id_fields = ('author',)

admin.site.register(Post, PostAdmin)






