#在這裡定義序列化器:Django Rest FrameWork提供的功能，可以將Django數據模型序列化成相對應的JSON格式
from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = (
            'id', 'name', 'ingredients', 'picture',
            'difficulty', 'prep_time', 'prep_guide'
        )