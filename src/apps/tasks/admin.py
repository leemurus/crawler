from django.contrib import admin
from .models import CrawlerTask


@admin.register(CrawlerTask)
class CrawlerTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_id', 'url')
    ordering = ('id',)
