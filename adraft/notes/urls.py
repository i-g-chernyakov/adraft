from django.urls import path, include

from .views import NoteListView, NoteDetailView, NoteEditView, NoteCreateView, NoteDeleteView
from .views import get_attachment, AttachmentListView, AttachmentDetailView
from .views import AttachmentCreateView, AttachmentEditView, AttachmentDeleteView


app_name = 'notes'
attachments_patterns = [
    path('^$', AttachmentListView.as_view(), name='attachment_index'),
    path('^(?P<int:pk>[0-9]+)/attachment/$', get_attachment, name='attachment_attachment'),
    path('^(?P<pk>[0-9]+)/$', AttachmentDetailView.as_view(), name='attachment_detail'),
    path('^create/$', AttachmentCreateView.as_view(), name='attachment_create'),
    path('^(?P<pk>[0-9]+)/edit/$', AttachmentEditView.as_view(), name='attachment_edit'),
    path('^(?P<pk>[0-9]+)/delete/$', AttachmentDeleteView.as_view(), name='attachment_delete'),
]

urlpatterns = [
    path(r'^$', NoteListView.as_view(), name='home'),
    path(r'^create/$', NoteCreateView.as_view(), name='create'),
    path(r'^(?P<pk>[0-9]+)/$', NoteDetailView.as_view(), name='detail'),
    path(r'^(?P<pk>[0-9]+)/edit/$', NoteEditView.as_view(), name='edit'),
    path(r'^(?P<pk>[0-9]+)/delete/$', NoteDeleteView.as_view(), name='delete'),
    path(r'^attachments/', include(attachments_patterns)),
]
