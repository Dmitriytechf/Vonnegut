from django.db import models


class  VonnegutFact(models.Model):
    text = models.TextField(verbose_name="Текст факта")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    class Meta:
        verbose_name = "Факт о Воннегуте"
        verbose_name_plural = "Факты о Воннегуте"
    
    def __str__(self):
        return self.text
