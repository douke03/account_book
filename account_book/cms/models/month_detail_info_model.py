"""this is model class"""
from datetime import datetime
from django.db import models
from cms.models.common_field_model import CommonField
from cms.models.detail_item_model import DetailItem


class MonthDetailInfo(CommonField):
    """月別詳細情報テーブルを定義するためのクラス"""

    month_and_year = models.CharField('年月', max_length=6)
    detail_item = models.ForeignKey(
        DetailItem, on_delete=models.PROTECT, related_name='detail_item', verbose_name='項目')
    reporting_date = models.DateField('報告日', default=datetime.now)
    an_amount = models.DecimalField('金額', max_digits=14, decimal_places=3)
    supplement = models.CharField('備考', max_length=64, blank=True)

    class Meta:
        # テーブル名：month_detail_info
        db_table = 'month_detail_info'
        unique_together = ['month_and_year', 'detail_item']
        verbose_name = '月別詳細情報'
        verbose_name_plural = '月別詳細情報'

    def __str__(self):
        return self.month_and_year
