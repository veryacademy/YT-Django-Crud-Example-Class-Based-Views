from django.contrib import admin
from .models import Core


@admin.register(Core)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
