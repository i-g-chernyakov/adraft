from django.conf.urls import url

from .views import NoteDetailView, NoteListView

app_name = 'base'
urlpatterns = [
    url(r'', NoteListView.as_view(), name='note_list'),
    url(r'^(?P<id>[-\w]+)/$', NoteDetailView.as_view(), name='note_detail'),
    url(r'^(?P<id>[-\w]+)/$', NoteDetailView.as_view(), name='note_detail'),
]