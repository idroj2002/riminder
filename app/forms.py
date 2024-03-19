from django import forms
from app.models import Note, Reminder, Category


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'categories']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'description', 'reminder_date']
