from django.contrib import admin
from cms.models.detail_item_model import DetailItem
from cms.models.item_model import Item
from cms.models.month_detail_info_model import MonthDetailInfo
from cms.models.todo_model import ToDo


admin.site.register(Item)
admin.site.register(DetailItem)
admin.site.register(MonthDetailInfo)
admin.site.register(ToDo)
