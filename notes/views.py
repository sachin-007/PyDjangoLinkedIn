from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect

from .forms import NotesForm
# Create your views here.
from .models import Notes

from django.views.generic import CreateView,ListView,DetailView,UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class NotesCreateView(LoginRequiredMixin,CreateView):
    model = Notes
    # fields = ['title','text']
    success_url = "/smart/notes"
    form_class = NotesForm
    login_url="/admin"
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url()) 

class NotesListView(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url="/admin"
    
    def get_queryset(self):
        return self.request.user.notes.all()
    
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

class NotesUpdateView(UpdateView):
    model=Notes
    success_url = "/smart/notes"
    form_class= NotesForm
    
class NotesDeleteView(DeleteView):
    model=Notes
    success_url = "/smart/notes"
    template_name = "notes/notes_delete.html"
