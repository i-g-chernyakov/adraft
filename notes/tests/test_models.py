import pytest
from django.contrib.auth.models import User

from notes.models import Note


@pytest.mark.django_db
class TestNote:
    def setup(self):
        self.user = User.objects.create_user('john', 'john@email.com', 'john')
        self.user.save()

    def test_simple_note(self):
        note = Note.objects.create(
            title='note',
            annotation='annotation',
            text='text',
            user=self.user
        )
        note.save()
        assert note.html == '<div class="document">\n<p>text</p>\n</div>\n'
