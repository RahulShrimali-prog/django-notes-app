# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q

# Read - Notes List
@login_required(login_url='login')
def notes_list(request):
    query = request.GET.get('q', '')
    notes = Note.objects.filter(owner=request.user) if hasattr(Note, 'owner') else Note.objects.all()

    # Search - Query Notes
    if query:
        notes = notes.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    # Pagination - Limit Notes per Page
    paginator = Paginator(notes.order_by('-id'), 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'notes/notes_list.html', {
        'page_obj': page_obj,
        'q': query,
    })

# Create - Add New Note
@login_required(login_url='login')
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            messages.success(request, 'Note created!')
            return redirect('notes_list')
    else:
        form = NoteForm()
    return render(request, 'notes/create.html', {'form': form})


# Update - Edit Existing Note
@login_required(login_url='login')
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/update.html', {'form': form})

# Delete - Delete Note
@login_required(login_url='login')
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('notes_list')
    return render(request, 'notes/delete_note.html', {'note': note})
