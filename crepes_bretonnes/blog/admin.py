from django.contrib import admin
from .models import Category, Post
from django.utils.text import Truncator

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'date', 'display_excerpt')
	list_filter = ('author', 'category',)
	date_hierarchy = 'date'
	ordering = ('date',)
	search_fields = ('title', 'content')

	fieldsets = (
		('General', {
			'classes': ['collapse',],
			'fields': ('title', 'author', 'category')
		}),
		('Post content', {
			'description': 'Le formulaire accepte les balises HTML. Utilisez les à bon escient !',
			'fields': ('content',)
			}),
	)

	def display_excerpt(self, post):
		return Truncator(post.content).chars(40, truncate='...')


	display_excerpt.short_description = "Aperçu du contenu"

admin.site.register(Category)
admin.site.register(Post, PostAdmin)