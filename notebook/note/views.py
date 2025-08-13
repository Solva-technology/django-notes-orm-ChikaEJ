from django.shortcuts import render

from .models import Note


def all_notes(request):
    all_notes = Note.objects.all()
    context = {'all_notes': all_notes}
    return render(request, 'notes/all_notes.html', context)

def note_detail(request, note_id):
    note = Note.objects.get(id=note_id)
    context = {'note': note}
    return render(request, 'notes/note_detail.html', context)