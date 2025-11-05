from rest_framework import serializers

class SummarizerSerializer(serializers.Serializer):
    url = serializers.URLField()
