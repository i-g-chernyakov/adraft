from django import forms

from .models import Note


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ['title', 'annotation', 'text']

    class Media:
        js = ('https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.22.0/codemirror.js',
              'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.22.0/addon/mode/overlay.js',
              'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.22.0/mode/rst/rst.js',
              )
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.22.0/codemirror.css',
                    'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.22.0/theme/mbo.css')
        }

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['text'].initial = self.instance.text
        else:
            self.fields['text'].initial = '-'

    def save(self, commit=True):
        instance = super(NoteForm, self).save(commit)
        if commit:
            instance.text = self.cleaned_data['text']

        return instance
