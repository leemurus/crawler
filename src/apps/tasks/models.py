import datetime
import json
from typing import Optional
import uuid

from django.db import models
from django.db.models.functions import Now
from django_celery_results.models import TaskResult

from core import settings


class CrawlerTask(models.Model):
    task = models.OneToOneField(
        TaskResult, to_field='task_id', on_delete=models.CASCADE,
    )
    url = models.URLField(editable=False, db_index=True)

    @classmethod
    def get_task_info(cls, task_id: uuid.UUID) -> Optional[dict]:
        try:
            cr_task = cls.objects.select_related('task').get(task_id=task_id)
        except cls.DoesNotExist:
            return None

        return {
            'task_id': cr_task.task_id,
            'url': cr_task.url,
            'status': cr_task.task.status,
            'result': json.loads(cr_task.task.result),
        }

    @classmethod
    def get_last_task_by_url(cls, url: str) -> Optional['CrawlerTask']:
        cr_task = cls.objects.select_related('task').filter(
            url=url,
            task__date_done__gte=Now() - datetime.timedelta(
                seconds=settings.CACHE_FOR_URL_CRAWLING
            )
        ).order_by('task__date_done').last()

        return cr_task
