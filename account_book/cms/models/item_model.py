"""this is model class"""
from django.db import models
from cms.models.master_field_model import MasterField


class Item(MasterField):
    """項目テーブルを定義するためのクラス"""

    item_id = models.CharField('項目ID', max_length=8, unique=True)
    item_name = models.CharField('項目名', max_length=32)

    class Meta:
        # テーブル名：item
        db_table = 'item'
        verbose_name = '項目'
        verbose_name_plural = '項目'

    def __str__(self):
        return self.item_name
