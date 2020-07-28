#實現路由，使用視圖集，只需調用DefaultRouter自動生成相關路由
#加入紀錄路由映射列表urlpatterns中

from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'recipes', views.RecipeViewSet)

#router會為我們自動生成路由
# /recipes/:創建食譜POST方法，讀取食譜列表GET方法
# /recipes/{id}: 獲取單個食譜GET，更新單個食譜PUT或是刪除食譜DELETE

#Django路由定義中部包刮HTTP方法，具體HTTP方法可以在視圖中讀取並判斷
urlpatterns = [
    path('', include(router.urls)),
]