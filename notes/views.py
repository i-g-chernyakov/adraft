from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Note
from .forms import NoteForm


class NoteDetailView(DetailView):
    model = Note

    def get_context_data(self, **kwargs):
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        return context


class NoteEditView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(NoteEditView, self).form_valid(form)


class NoteListView(ListView):
    model = Note
    context_object_name = "note_list"


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NoteCreateView, self).form_valid(form)
