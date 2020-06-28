from django.contrib import admin
from .models import Postagem, Comment
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget



# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data')
    list_filter = ("autor",)
    image_field = ('arquivo')
    search_fields = ['titulo', 'descricao']
    prepopulated_fields = {'slug': ('titulo',)}
    
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)



# Apply summernote to specific fields.
class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'postagem', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Postagem, PostAdmin)
admin.site.register(Comment, CommentAdmin)


