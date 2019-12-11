from django.contrib import admin
# Register your models here.
from .models import Author, Genre, Book, Language, BookPdf

class AuthorInline(admin.TabularInline):
    model = Author
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'language')
admin.site.register(Book, BookAdmin)
inlines = [AuthorInline]


class LanguageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Language, LanguageAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'display_books')
    fields = ['first_name', 'last_name', 'date_of_birth']
admin.site.register(Author, AuthorAdmin)

admin.site.register(BookPdf)


class GenreAdmin(admin.ModelAdmin):
    pass
admin.site.register(Genre, GenreAdmin)
