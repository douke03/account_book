"""this is model class"""
from django.db import models
from cms.models.common_field_model import CommonField


class MasterField(CommonField):
    """マスタ用フィールドを定義するためのクラス"""

    is_active = models.BooleanField('有効', default=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.updated_by = kwargs['user']
        self.updated_at = kwargs['now']
        self.save()
