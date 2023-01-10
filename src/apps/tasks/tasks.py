import re
from urllib.parse import urljoin

from celery.signals import before_task_publish
from celery import states
from django.db import transaction
import requests

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
def crawl_page(main_url: str) -> list[str]:
    html_text = requests.get(main_url).text.replace('&amp;', '&')

    HTML_TAG_REGEX = re.compile(r'<a[^<>]+href=([\'\"])(.*?)\1')
    reg_urls = set(
        urljoin(main_url, match[1])
        for match in HTML_TAG_REGEX.findall(html_text)
    )

    return list(reg_urls)
