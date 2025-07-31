from django.contrib import admin
from .models import User, Note

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")

class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "category", "title", "content")
    
# Registering 
admin.site.register(User, UserAdmin)
admin.site.register(Note, NoteAdmin)
