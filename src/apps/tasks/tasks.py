from celery.signals import before_task_publish
from celery import states
from django.db import transaction

from .models import CrawlerTask
from core.celery import celery_app


@before_task_publish.connect
def create_task_row(
        body: tuple[tuple[str], dict, dict] = None,
        headers: dict = None,
        **kwargs,
):
    with transaction.atomic():
        celery_app.backend.store_result(
            task_id=headers['id'],
            state=states.PENDING,
            result=None,
        )

        url: str = body[0][0]
        CrawlerTask.objects.create(
            task_id=headers['id'],
            url=url,
        )


@celery_app.task(name='crawl_page')
def crawl_page(task_id):
    print(task_id)

    import time
    time.sleep(5)

    return ['google.com', 'vk.com', 'ebay.com']
