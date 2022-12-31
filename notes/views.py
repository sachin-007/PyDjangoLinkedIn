from django.shortcuts import render
from django.http import Http404

# Create your views here.
from .models import Notes

from django.views.generic import CreateView,ListView,DetailView


class NotesCreateView(CreateView):
    model = Notes
    fields = ['title','text']
    success_url = "/smart/notes"


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/note_detail.html"


def detail(request,pk):
    try:
        note=Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("note that you are finding is not exist / valid")
    return render(request,'notes/note_detail.html',{'note':note})