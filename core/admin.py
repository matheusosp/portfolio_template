from django.contrib import admin
from core.models import Projects


@admin.register(Projects)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'resume')
