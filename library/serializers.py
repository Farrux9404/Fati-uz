from rest_framework import serializers
from library.models import Dissertationabstract, Category, JournalUzbekistan


class DissertationabstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dissertationabstract
        fields = ['title', 'image', 'status']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'status', 'order']


class JournalUzbekistanSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalUzbekistan
        fields = ['title', 'status', 'order']