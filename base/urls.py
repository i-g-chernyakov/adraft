from django.conf.urls import url

from .views import NoteListView, NoteDetailView, NoteEditView, NoteCreateView


app_name = 'base'
urlpatterns = [
    url(r'^$', NoteListView.as_view(), name='home'),
    url(r'^create/$', NoteCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', NoteDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', NoteEditView.as_view(), name='edit'),
]