from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Note


class NoteDetailView(DetailView):
    model = Note

    def get_context_data(self, **kwargs):
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        return context


class NoteListView(ListView):
    model = Note
