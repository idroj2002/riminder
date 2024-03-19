from app.models import Note, Category, Reminder
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from app.forms import NoteForm, ReminderForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note_list.html', {'notes': notes})


def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'note_detail.html', {'note': note})


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form})


def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'edit_note.html', {'form': form})


def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'delete_note.html', {'note': note})


def reminder_list(request):
    reminders = Reminder.objects.all()
    return render(request, 'reminder_list.html', {'reminders': reminders})


def reminder_detail(request, reminder_id):
    reminder = get_object_or_404(Reminder, pk=reminder_id)
    return render(request, 'reminder_detail.html', {'reminder': reminder})


def create_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reminder_list')
    else:
        form = ReminderForm()
    return render(request, 'create_reminder.html', {'form': form})


def edit_reminder(request, reminder_id):
    reminder = get_object_or_404(Reminder, pk=reminder_id)
    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = ReminderForm(instance=reminder)
    return render(request, 'edit_reminder.html', {'form': form})


def delete_reminder(request, reminder_id):
    reminder = get_object_or_404(Reminder, pk=reminder_id)
    if request.method == 'POST':
        reminder.delete()
        return redirect('note_list')
    return render(request, 'delete_reminder.html', {'reminder': reminder})


def base(request):
    return render(request, 'base.html')

<<<<<<< HEAD
def home(request):
    return render(request, 'home.html')
=======
>>>>>>> 1e6164b74d3b503ccc2ec8c6386e949e49ac8e47

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al usuario a la página de inicio de sesión después del registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
