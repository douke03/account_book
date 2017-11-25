"""this is model class"""
from django.db import models
from cms.models.item_model import Item
from cms.models.master_field_model import MasterField


class DetailItem(MasterField):
    """詳細項目テーブルを定義するためのクラス"""

    item = models.ForeignKey(Item, verbose_name='親項目', related_name='item')
    detailed_item_id = models.CharField('詳細項目ID', max_length=8)
    detailed_item_name = models.CharField('詳細項目名', max_length=32)

    class Meta:
        # テーブル名：detailed_item
        db_table = 'detail_item'
        unique_together = ['item', 'detailed_item_id']
        verbose_name = '詳細項目'
        verbose_name_plural = '詳細項目'

    def __str__(self):
        return self.detailed_item_name
