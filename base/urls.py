from django.conf.urls import url

from .views import NoteDetailView

app_name = 'base'
urlpatterns = [
    url(r'^(?P<id>[-\w]+)/$', NoteDetailView.as_view(), name='note-detail'),
]