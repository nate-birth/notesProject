from django.shortcuts import render, redirect
from .forms import NoteForm, DescForm
from .models import *

# Homepage
def index(request):
    context = {
        'notes': Note.objects.all(),
        'note_form':  NoteForm(),
        'desc_form': DescForm(),
    }
    return render(request, 'notes/index.html', context)

## Create
# Create Note
def note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid() == False:
            context = {
                'notes': Note.objects.all(),
                'note_form':  form,
                'desc_form': DescForm(),
            }
            return render(request, 'notes/notes_index.html', context)
        else:
            form.save()
            print(form)
    context = {
        'notes': Note.objects.all(),
        'note_form':  NoteForm(),
        'desc_form': DescForm(),
    }
    return render(request, 'notes/notes_index.html', context)

# Create Description for note
def description(request):
    if request.method == 'POST':
        form = DescForm(request.POST)
        if form.is_valid() == False:
            context = {
                'notes': Note.objects.all(),
                'note_form':  NoteForm(),
                'desc_form': form,
            }
            return render(request, 'notes/index.html', context)
        else:
            get_note = Note.objects.get(id=request.POST['n_id'])
            obj = Description.objects.create(content=request.POST['content'],note=get_note)
    context = {
        'notes': Note.objects.all(),
        'note_form':  NoteForm(),
        'desc_form': DescForm(),
    }
    return render(request, 'notes/notes_index.html', context)

## Update
def update(request):
    if request.method == 'POST':
        desc = Description.objects.get(id=request.POST['d_id'])
        update_content = request.POST['content']
        desc.content = update_content
        desc.save()
    context = {
        'notes': Note.objects.all(),
        'note_form':  NoteForm(),
        'desc_form': DescForm(),
    }
    return render(request, 'notes/notes_index.html', context)

## Delete
def delete(request):
    if request.method == 'POST':
        print(request.POST['k_id'])
        note_delete = Note.objects.get(id=request.POST['k_id'])
        note_delete.delete()
    context = {
        'notes': Note.objects.all(),
        'note_form':  NoteForm(),
        'desc_form': DescForm(),
    }
    return render(request, 'notes/notes_index.html', context)

