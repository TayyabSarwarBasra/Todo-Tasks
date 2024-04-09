from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)


class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'deadline', 'priority', 'status', 'category']


admin.site.register(Todo, TodoAdmin)