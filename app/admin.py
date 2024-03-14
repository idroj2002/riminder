from django.contrib import admin
from app.models import Note, Reminder, Category


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'creation_date', 'modification_date')
    list_filter = ('creation_date', 'modification_date')
    search_fields = ('title', 'content')


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'reminder_date']
    list_filter = ['reminder_date']
    search_fields = ('title', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
