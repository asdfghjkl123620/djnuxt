from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RecipeSerializer
from .models import Recipe
# Create your views here.
#調用模型視圖集，搞定數據模型增刪修查


class RecipeViewSet(viewsets.ModelViewSet):
    '''
    只需指定serializer_class序列器類和queryset模型查詢集集可自訂一好模型的增刪修查
    '''
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()