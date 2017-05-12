from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from sendfile import sendfile
from django.contrib.auth.decorators import login_required

from .models import Note, Attachment
from .forms import NoteForm, AttachmentForm, AttachmentEditForm


class NoteListView(ListView):
    model = Note
    context_object_name = "note_list"


class NoteDetailView(DetailView):
    model = Note
    context_object_name = "note"

    def get_context_data(self, **kwargs):
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        return context


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NoteCreateView, self).form_valid(form)


class NoteEditView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    raise_exception = True

    def has_permission(self):
        obj_user = self.get_object().user
        req_user = self.request.user
        return (obj_user == req_user)


class NoteDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('notes:home')

    def has_permission(self):
        obj_user = self.get_object().user
        req_user = self.request.user
        return (obj_user == req_user)


@login_required
def get_attachment(request, pk):
    attachment = get_object_or_404(Attachment, pk=pk)
    as_attachment = not attachment.is_image()
    return sendfile(
        request,
        attachment.file.path,
        attachment=as_attachment
    )


class AttachmentListView(ListView):
    model = Attachment
    context_object_name = "attachments"


class AttachmentDetailView(DetailView):
    model = Attachment
    context_object_name = "attachment"

    def get_context_data(self, **kwargs):
        context = super(AttachmentDetailView, self).get_context_data(**kwargs)
        return context


class AttachmentCreateView(LoginRequiredMixin, CreateView):
    model = Attachment
    form_class = AttachmentForm

    def __init__(self, **kwargs):
        self.request = None
        super().__init__(**kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AttachmentCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST, self.request.FILES)
        if form.is_valid():
            form.instance.user = self.request.user
            form.instance.file = self.request.FILES['file']
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class AttachmentEditView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Attachment
    form_class = AttachmentEditForm
    raise_exception = True

    def has_permission(self):
        obj_user = self.get_object().user
        req_user = self.request.user
        return (obj_user == req_user)


class AttachmentDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Attachment
    success_url = reverse_lazy('notes:attachment_index')
