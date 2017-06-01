from rest_framework import generics, permissions


from .serializers import NoteSerializer
from .models import Note
from .permissions import NoteAuthorCanEditPermission


class NoteMixin(object):
    model = Note
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [
        NoteAuthorCanEditPermission
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NoteList(NoteMixin, generics.ListCreateAPIView):
    pass


class NoteDetail(NoteMixin, generics.RetrieveUpdateDestroyAPIView):
    pass
