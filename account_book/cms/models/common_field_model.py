"""this is model class"""
import uuid
from django.contrib.auth.models import User
from django.db import models


class CommonField(models.Model):
    """共通フィールドを定義するためのクラス"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(
        User, related_name='%(app_label)s_%(class)s_created_by', verbose_name='作成者')
    created_at = models.DateTimeField('作成日', blank=True, null=True)
    updated_by = models.ForeignKey(
        User, related_name='%(app_label)s_%(class)s_updated_by', verbose_name='更新者', blank=True, null=True)
    updated_at = models.DateTimeField('更新日', blank=True, null=True)

    class Meta:
        abstract = True
