from django.contrib import admin
from .models import CustomUser, Note, Todo, Category, Tag

# Register your models here.
admin.site.register(Note)
admin.site.register(Todo)
admin.site.register(Category)
admin.site.register(Tag)