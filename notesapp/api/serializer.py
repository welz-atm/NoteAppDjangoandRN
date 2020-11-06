from rest_framework import serializers
from notesapp.models import Note


class NoteSerializer(serializers.ModelSerializer):
    display_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Note
        fields = ['pk', 'date_created', 'date_published', 'title', 'description', 'is_published', 'author',
                  'display_name', ]