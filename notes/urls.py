from django.conf.urls import url, include

from .views import NoteListView, NoteDetailView, NoteEditView, NoteCreateView, NoteDeleteView
from .views import get_attachment, AttachmentListView, AttachmentDetailView
from .views import AttachmentCreateView, AttachmentEditView, AttachmentDeleteView


app_name = 'notes'
attachments_patterns = [
    url(r'^$', AttachmentListView.as_view(), name='attachment_index'),
    url(r'^(?P<pk>[0-9]+)/attachment/$', get_attachment, name='attachment_attachment'),
    url(r'^(?P<pk>[0-9]+)/$', AttachmentDetailView.as_view(), name='attachment_detail'),
    url(r'^create/$', AttachmentCreateView.as_view(), name='attachment_create'),
    url(r'^(?P<pk>[0-9]+)/edit/$', AttachmentEditView.as_view(), name='attachment_edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', AttachmentDeleteView.as_view(), name='attachment_delete'),
]

urlpatterns = [
    url(r'^$', NoteListView.as_view(), name='home'),
    url(r'^create/$', NoteCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', NoteDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', NoteEditView.as_view(), name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', NoteDeleteView.as_view(), name='delete'),
    url(r'^attachments/', include(attachments_patterns)),
]
