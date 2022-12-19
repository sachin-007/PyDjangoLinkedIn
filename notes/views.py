from django.shortcuts import render
from django.http import Http404

# Create your views here.
from .models import Notes

def list(request):
    all_notes= Notes.objects.all()
    return render(request,'notes/notes_list.html',{'notes':all_notes})

def detail(request,pk):
    try:
        note=Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("note that you are finding is not exist / valid")
    return render(request,'notes/note_detail.html',{'note':note})