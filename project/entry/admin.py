from django.contrib import admin
from .models import *
# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    list_display = ('entry_name','user', 'created_at')
    list_display_links = ('user', 'entry_name')

class EntryCommentsAdmin(admin.ModelAdmin):
    list_display = ('commented_entry','writer', 'created_at')
    list_display_links = ('writer', 'commented_entry')

admin.site.register(Entry,EntryAdmin)
admin.site.register(EntryComments,EntryCommentsAdmin)