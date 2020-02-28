from django.contrib import admin
from .models import Postagem

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data')
    list_filter = ("autor",)
    search_fields = ['titulo', 'descricao']
    prepopulated_fields = {'slug': ('titulo',)}

admin.site.register(Postagem, PostAdmin)

