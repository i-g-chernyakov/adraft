from rest_framework import serializers

from .models import Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note.user.model
        fields = ('id', 'username')


class NoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    def get_validation_exclusions(self):
        exclusions = super(NoteSerializer, self).get_validation_exclusions()
        return exclusions + ['user']

    class Meta:
        model = Note
        fields = '__all__'
