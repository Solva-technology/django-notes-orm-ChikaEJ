from django.shortcuts import render, get_object_or_404

from .models import Note


def all_notes(request):
    all_notes = Note.objects.select_related('author', 'status').prefetch_related('categories').order_by('-created_at')
    context = {'all_notes': all_notes}
    return render(request, 'notes/all_notes.html', context)

def note_detail(request, note_id):
    note = get_object_or_404(
        Note
        .objects
        .select_related('author', 'status')
        .prefetch_related('categories'),
        pk=note_id
    )
    context = {'note': note}
    return render(request, 'notes/note_detail.html', context)