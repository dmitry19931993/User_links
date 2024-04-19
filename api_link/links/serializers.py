from rest_framework import serializers


class LinkSerializer(serializers.Serializer):
    """Сериализатор для ссылок"""

    title = serializers.CharField(max_length=512)
    description = serializers.CharField()
    link = serializers.URLField(max_length=512)
    image = serializers.URLField(max_length=512)
    type = serializers.CharField(max_length=512, default='website')


class CollectionSerializer(serializers.Serializer):
    """Сериализатор для коллекций"""

    name = serializers.CharField(max_length=512)
    description = serializers.CharField()