from os import path
from uuid import uuid4
import re

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.deconstruct import deconstructible
from django.template.defaultfilters import filesizeformat
from django.urls import reverse
import magic
import markups

from utils import get_class_name_plural


USER_MODEL = getattr(settings, 'AUTH_USER_MODEL')


@deconstructible
class FileValidator(object):
        error_messages = {
            'value_type': _('Incorrect type of object. Type of object must be models.FileField. '
                            'But type of object is %(type)s'),
            'max_size': _('Ensure this file size is not greater than %(max_size)s. '
                          'Your file size is %(size)s.'),
            'min_size': _('Ensure this file is not less than %(min_size)s. '
                          'Your file size is %(size)s.'),
            'content_type': _('Files of type %(content_type)s are not supported.'),
        }

        def __init__(self, max_size=None, min_size=None, content_types=()):
            self.max_size = max_size
            self.min_size = min_size
            self.content_types = content_types

        def __call__(self, file):
            if not isinstance(file, models.FileField):
                params = {
                    'type': type(file),
                }
                raise ValidationError(self.error_messages['value_type'],
                                      'type', params)

            if self.max_size is not None and file.size > self.max_size:
                params = {
                    'max_size': filesizeformat(self.max_size),
                    'size': filesizeformat(file.size),
                }
                raise ValidationError(self.error_messages['max_size'],
                                      'max_size', params)

            if self.min_size is not None and file.size < self.min_size:
                params = {
                    'min_size': filesizeformat(self.min_size),
                    'size': filesizeformat(file.size),
                }
                raise ValidationError(self.error_messages['min_size'],
                                      'min_size', params)

            if self.content_types:
                content_type = magic.from_buffer(file.read(), mime=True)
                if content_type not in self.content_types:
                    params = {'content_type': content_type}
                    raise ValidationError(self.error_messages['content_type'],
                                          'content_type', params)

        def __eq__(self, other):
            return (
                isinstance(other, FileValidator) and
                self.max_size == other.max_size and
                self.min_size == other.min_size and
                self.content_types == other.content_types
            )

        def __ne__(self, other):
            return not (self == other)


validate_attachment = FileValidator(min_size=10,
                                    max_size=1024*1024*10,
                                    content_types=(
                                        'application/pdf',
                                        'application/postscript',
                                        'application/x-tex',
                                        'application/vnd.oasis.opendocument.text',
                                        'application/vnd.oasis.opendocument.spreadsheet',
                                        'application/vnd.oasis.opendocument.presentation',
                                        'application/vnd.oasis.opendocument.graphics',
                                        'application/vnd.ms-excel',
                                        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                                        'application/vnd.ms-powerpoint',
                                        'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                                        'application/msword',
                                        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                                        'application/x-dvi',
                                        'application/x-latex',
                                        'application/zip',
                                        'application/gzip',
                                        'text/csv',
                                        'text/html',
                                        'text/plain',
                                    ))


validate_image = FileValidator(min_size=10,
                               max_size=1024*1024*5,
                               content_types=(
                                   'image/gif',
                                   'image/jpeg',
                                   'image/pjpeg',
                                   'image/png',
                                   'image/svg+xml',
                                   'image/tiff',
                                   'image/vnd.microsoft.icon',
                                   'image/vnd.wap.bmp',
                               ))


def get_upload_to(instance, filename):
    """File will be uploaded to MERDIA_ROOT/user_id<user.id> or all/class_name_plural/%Y/%m/%d/uuid4

    We change name of downloaded file to uuid4.
    :param instance:
    :param filename:
    :return: path to upload file
    """
    try:
        user = instance.user
    except AttributeError:
        subfolder = 'all'
    else:
        subfolder = 'user_id{0}'.format(user.id)

    return path.join(subfolder,
                     get_class_name_plural(instance),
                     '%Y/%m/%d',
                     str(uuid4()),
                     path.splitext(filename)[-1])


class Note(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=100)
    annotation = models.CharField(verbose_name=_('Annotation'), max_length=200, blank=True)
    text = models.TextField(verbose_name=_('Text'))
    html = models.TextField(verbose_name=_('HTML'), blank=True, default='')
    user = models.ForeignKey(USER_MODEL, related_name='%(class)s_users', verbose_name=_('Author'))
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Note')
        verbose_name_plural = _('Notes')

    def save(self, *args, **kwargs):
        self.html = self.convert()
        super(Note, self).save(*args, **kwargs)

    @staticmethod
    def get_markup_instance():
        return markups.ReStructuredTextMarkup()

    @property
    def markup(self):
        if not hasattr(self, '__markup_instance'):
            self.__markup_instance = Note.get_markup_instance()
        return self.__markup_instance

    def convert(self):
        html = self.markup.convert(self.text).get_document_body()
        html = self._sanitize(html)
        return html

    @property
    def stylesheet(self):
        return self.markup.get_stylesheet()

    @property
    def javascript(self):
        return self.markup.get_javascript()

    def _sanitize(self, html):
        """ Remove all scripts from html

        :param html:
        :return: html without scripts
        """
        return re.sub(r'<script.*?</script>', '', html, flags=re.MULTILINE)

    def get_absolute_url(self):
        return reverse('base:detail', kwargs={'pk': self.pk})


class Attachment(models.Model):
    def upload_to(self, filename):
        """Attachment will be uploaded to MEDIA_ROOT/attachments/user_<id>/<filename>

        :return: path to attachment file
        """
        return 'attachments/user_{0}/{1}.{2}'.format(self.user.id, uuid4(), path.splitext(filename)[-1])

    user = models.ForeignKey(USER_MODEL, related_name='attachment_user', verbose_name=_('Attachment'))
    title = models.CharField(verbose_name=_('Title'), max_length=100)
    description = models.CharField(verbose_name=_('Description'), max_length=255)
    file = models.FileField(upload_to=get_upload_to, max_length=150, validators=[validate_attachment])

    class Meta:
        verbose_name = _('Attachment')
        verbose_name_plural = _('Attachments')

    def __str__(self):
        return self.title

    def name(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Attachment, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete(save=False)
        super(Attachment, self).delete(*args, **kwargs)


class Image(models.Model):
    user = models.ForeignKey(USER_MODEL, related_name='image_user', verbose_name=_('Attachment'))
    title = models.CharField(verbose_name=_('Title'), max_length=100)
    description = models.CharField(verbose_name=_('Description'), max_length=255)
    image = models.ImageField(upload_to=get_upload_to, validators=[validate_image])

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    def __str__(self):
        return self.title