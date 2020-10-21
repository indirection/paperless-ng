from rest_framework import serializers

from .models import Correspondent, Tag, Document, Log, DocumentType


class CorrespondentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Correspondent
        fields = (
            "id",
            "slug",
            "name",
            "automatic_classification"
        )


class DocumentTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DocumentType
        fields = (
            "id",
            "slug",
            "name",
            "automatic_classification"
        )


class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = (
            "id",
            "slug",
            "name",
            "colour",
            "automatic_classification",
            "is_inbox_tag"
        )


class CorrespondentField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Correspondent.objects.all()


class TagsField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Tag.objects.all()


class DocumentTypeField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return DocumentType.objects.all()


class DocumentSerializer(serializers.ModelSerializer):

    correspondent_id = CorrespondentField(allow_null=True, source='correspondent')
    tags_id = TagsField(many=True, source='tags')
    document_type_id = DocumentTypeField(allow_null=True, source='document_type')

    class Meta:
        model = Document
        depth = 1
        fields = (
            "id",
            "correspondent",
            "correspondent_id",
            "document_type",
            "document_type_id",
            "title",
            "content",
            "file_type",
            "tags",
            "tags_id",
            "checksum",
            "created",
            "modified",
            "added",
            "file_name",
            "download_url",
            "thumbnail_url",
            "archive_serial_number"
        )


class LogSerializer(serializers.ModelSerializer):

    time = serializers.DateTimeField()
    messages = serializers.CharField()

    class Meta:
        model = Log
        fields = (
            "time",
            "messages"
        )
