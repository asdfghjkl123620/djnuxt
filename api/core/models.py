from django.db import models

# Create your models here.



class Recipe(models.Model):
    DIFFICULTY_LEVELS = (
        ('Easy', '容易'),
        ('Medium', '中等'),
        ('Hard', '困難'),
    )
    name = models.CharField(max_length=120, verbose_name='名稱')
    ingredients = models.CharField(max_length=400, verbose_name='食材')
    picture = models.FileField(verbose_name='圖片')
    difficulty = models.CharField(choices=DIFFICULTY_LEVELS, max_length=10,verbose_name='製作難度')
    prep_time = models.PositiveIntegerField(verbose_name='準備時間',default='20')
    prep_guide = models.TextField(verbose_name='製作指南',default='hello this is default cookbooks')
    class Meta:
        """
        定義Recipe的原數據
        """
        verbose_name = '食譜'
        verbose_name_plural = '食譜'
    def __str__(self):
        """
        定義菜譜對象轉換為String該如何顯示
        """
        return '{}的食譜'.format(self.name)