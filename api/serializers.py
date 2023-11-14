from rest_framework import serializers
from api.models import Post, Comment


class postModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class commentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

        