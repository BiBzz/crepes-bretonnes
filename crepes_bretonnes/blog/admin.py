from django.contrib import admin
from .models import Post, Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ( 'title', 'author', 'date' )
	list_filter = ( 'author', 'category', )
	date_hierarchy = 'date'
	ordering = ( 'date', )
	search_fields = ( 'titre', 'contenu' )


admin.site.register(Category)
admin.site.register(Post, PostAdmin)