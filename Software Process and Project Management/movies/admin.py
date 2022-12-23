from django.contrib import admin
from .models import Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
	list_display = ('name', 'genre', 'year')
	search_fields = ['name', 'genre']

admin.site.register(Movie, MovieAdmin)