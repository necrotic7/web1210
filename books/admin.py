from django.contrib import admin
from .models import Book


@admin.register(Book) ##等同於->admin.site.register(Book,BookAdmin)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    search_fields = ['name']
    list_filter = ['price']


