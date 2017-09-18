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
    title = models.TextField('タイトル', validators=[MaxLengthValidator(32)])
    text = models.TextField('内容', blank=True)
    situation = models.TextField(
        '対応状況', validators=[MaxLengthValidator(32)], blank=True)
    priority = models.IntegerField('優先順位', choices=PRIORITY_CHOICES, default=4)
    is_complete = models.BooleanField('完了', default=False)

    class Meta:
        # テーブル名：todo
        db_table = 'todo'
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDo'

    def __str__(self):
        return self.title
