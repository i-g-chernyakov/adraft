from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Note, Attachment


CODEMIRROR = 'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.23.0/'


class NoteForm(forms.ModelForm):
    title = forms.CharField(label=_('Title'), widget=forms.TextInput(attrs={'size': '100%'}))
    annotation = forms.CharField(label=_("Annotation"),
                                 widget=forms.TextInput(attrs={'size': '100%'}))

    class Meta:
        model = Note
        fields = ['title', 'annotation', 'text']

    class Media:
        js = (''.join([CODEMIRROR, 'codemirror.min.js']),
              ''.join([CODEMIRROR, 'addon/mode/overlay.min.js']),
              ''.join([CODEMIRROR, 'addon/mode/xml/xml.min.js']),
              ''.join([CODEMIRROR, 'addon/display/fullscreen.min.js']),
              ''.join([CODEMIRROR, 'mode/rst/rst.js']),
              )
        css = {
            'all': (''.join([CODEMIRROR, 'codemirror.min.css']),
                    ''.join([CODEMIRROR, 'addon/display/fullscreen.css']),
                    ''.join([CODEMIRROR, 'theme/mbo.css']),
                    )
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


class AttachmentForm(forms.ModelForm):
    file = forms.FileField()

    class Meta:
        model = Attachment
        fields = ['title', 'description']


class AttachmentEditForm(forms.ModelForm):

    class Meta:
        model = Attachment
        fields = ['title', 'description']
