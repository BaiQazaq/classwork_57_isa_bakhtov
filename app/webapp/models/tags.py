from django.db import models


class Tag(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Тэг'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    update_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )
    
    def __str__(self):
        return self.name