from django.contrib import admin
from core.models import Projects, Categories


@admin.register(Projects)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'resume')


@admin.register(Categories)
class Categories(admin.ModelAdmin):
    list_display = ('id', 'name')