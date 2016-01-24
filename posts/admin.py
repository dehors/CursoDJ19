from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title","updated","timestamp"] # campos a mostrar
	list_display_links = ["updated"] #campo link para editar
	list_editable = ["title"]#campo editable
	list_filter = ["updated","timestamp"]#filtros de fechas en la parte derecha

	search_fields = ["title","content"]#buscador
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)