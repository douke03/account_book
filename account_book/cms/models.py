"""this is models class."""
from django.db import models
from datetime import datetime
from django.contrib import admin
from django.contrib.auth.models import User


class CommonField(models.Model):
    """共通フィールドを定義するためのクラス"""

    created_at = models.DateTimeField('作成日', default=datetime.now)
    created_by = models.ForeignKey(User, verbose_name='作成者')
    updated_at = models.DateTimeField('更新日', blank=True, null=True)
    updated_by = models.CharField('更新者', max_length=1, blank=True)
    def save(self, *args, **kwargs):
        print(self.id)
        if self.id:
            self.updated_at = datetime.now()
            print('if')
        else:
            self.updated_at = None
            print('else')
        super(CommonField, self).save(*args, **kwargs)
    class Meta:
        abstract = True


class MasterField(CommonField):
    """マスタ用フィールドを定義するためのクラス"""

    is_active = models.BooleanField('有効', default=True)
    class Meta:
        abstract = True


class Item(MasterField):
    """項目テーブルを定義するためのクラス"""

    item_id = models.CharField('項目ID', max_length=8, unique=True)
    item_name = models.CharField('項目名', max_length=32)
    class Meta:
        #テーブル名：item
        db_table = 'item'
        verbose_name = '項目'
        verbose_name_plural = '項目'
    def __str__(self):
        return self.item_name


class DetailItem(MasterField):
    """詳細項目テーブルを定義するためのクラス"""

    item = models.ForeignKey(Item, verbose_name='親項目', related_name='item')
    detailed_item_id = models.CharField('詳細項目ID', max_length=8)
    detailed_item_name = models.CharField('詳細項目名', max_length=32)
    class Meta:
        #テーブル名：detailed_item
        db_table = 'detail_item'
        unique_together = ['item', 'detailed_item_id']
        verbose_name = '詳細項目'
        verbose_name_plural = '詳細項目'
    def __str__(self):
        return self.detailed_item_name


class MonthDetailInfo(CommonField):
    """月別詳細情報テーブルを定義するためのクラス"""

    month_and_year = models.CharField('年月', max_length=6)
    detailed_item = models.ForeignKey(DetailItem, verbose_name='項目', related_name='detailed_item')
    reporting_date = models.DateField('報告日', default=datetime.now)
    an_amount = models.DecimalField('金額', max_digits=14, decimal_places=3)
    supplement = models.CharField('備考', max_length=64, blank=True)
    class Meta:
        #テーブル名：month_detail_info
        db_table = 'month_detail_info'
        unique_together = ['month_and_year', 'detailed_item']
        verbose_name = '月別詳細情報'
        verbose_name_plural = '月別詳細情報'
    def __str__(self):
        return self.month_and_year


class ToDoList(CommonField):
    """ToDoリストテーブルを定義するためのクラス"""

    title = models.CharField('タイトル', max_length=32, default=None)
    text = models.TextField('内容', blank=True)
    is_complete = models.BooleanField('完了', default=False)
    class Meta:
        #テーブル名：to_do_list
        db_table = 'to_do_list'
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDo'
    def __str__(self):
        return self.title
