from django.contrib import admin
from cms.models import Item, DetailItem, MonthDetailInfo, ToDoList

# Register your models here.

admin.site.register(Item)
admin.site.register(DetailItem)
admin.site.register(MonthDetailInfo)
admin.site.register(ToDoList)
