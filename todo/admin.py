from django.contrib import admin
from .models import TodoList, TodoList_files, TodoList_images

# Register your models here. 

class TodoList_filesInline(admin.StackedInline):
    model = TodoList_files

class TodoList_imageInline(admin.StackedInline):
    model = TodoList_images

class TodoListAdmin(admin.ModelAdmin):
    inlines = [TodoList_filesInline, TodoList_imageInline]
    list_display = ('name', 'description', 'date_created', 'date_deadline', 'remaining_days')
    list_filter = ['date_created']

class TodoList_imagesAdmin(admin.ModelAdmin):
    model = TodoList_images 

class TodoList_filesAdmin(admin.ModelAdmin):
    model = TodoList_files

admin.site.register(TodoList, TodoListAdmin)