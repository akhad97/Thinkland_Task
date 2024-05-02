from rest_framework import serializers 
from .models import Category



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'guid',
            'title',
            'description',
            'image',
        )


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'title',
            'description',
            'image',
        )
