"""this is model class"""
from django.db import models
from cms.models.master_field_model import MasterField
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator


class ToDo(MasterField):
    """ToDoを定義するためのクラス"""

    PRIORITY_CHOICES = (
        (1, 'Immediate'),
        (2, 'Urgent'),
        (3, 'High'),
        (4, 'Normal'),
        (5, 'Low'),
    )
    title = models.CharField('タイトル', max_length=64)
    text = models.TextField('内容', blank=True)
    correspondence_contents = models.TextField('対応内容', blank=True)
    correspondence_situation = models.TextField('対応状況', blank=True)
    priority = models.IntegerField('優先度', choices=PRIORITY_CHOICES, default=4)
    deadline = models.DateField('締切', blank=True, null=True)
    resolved_date = models.DateField('解決日', blank=True, null=True)
    is_complete = models.BooleanField('完了', default=False)

    class Meta:
        # テーブル名：todo
        db_table = 'todo'
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDo'

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.updated_by = kwargs['user']
        self.updated_at = kwargs['now']
        self.save()
