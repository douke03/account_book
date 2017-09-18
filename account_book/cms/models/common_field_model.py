"""this is model class"""
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class CommonField(models.Model):
    """共通フィールドを定義するためのクラス"""

    created_at = models.DateTimeField('作成日', default=datetime.now)
    created_by = models.ForeignKey(
        User, related_name='%(app_label)s_%(class)s_created_by', verbose_name='作成者')
    updated_at = models.DateTimeField('更新日', blank=True, null=True)
    updated_by = models.ForeignKey(
        User, related_name='%(app_label)s_%(class)s_updated_by', verbose_name='更新者', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.id:
            self.updated_at = datetime.now()
        else:
            self.updated_at = None
        super(CommonField, self).save(*args, **kwargs)

    class Meta:
        abstract = True
