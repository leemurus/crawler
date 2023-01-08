import uuid

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .tasks import crawl_page
from .models import CrawlerTask


@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer,))
@ensure_csrf_cookie  # add csrf token to the cookie
def get_search_page(request) -> Response:
    return Response(template_name='search.html')


@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer,))
@ensure_csrf_cookie  # add csrf token to the cookie
def get_task_page(request, task_id) -> Response:
    return Response(template_name='task.html')


@api_view(['POST'])
def start_crawler_task(request) -> Response:
    url = request.data.get('url')

    # Validate url
    url_validator = URLValidator()
    try:
        url_validator(url)
    except ValidationError:
        return Response(status=400)

    cr_task = CrawlerTask.get_last_task_by_url(url)
    if not cr_task:
        cr_task = crawl_page.delay(url)

    return Response(
        data={'task_id': cr_task.task_id}
    )


@api_view(['GET'])
def get_task_info(request, task_id: uuid.UUID) -> Response:
    task_info = CrawlerTask.get_task_info(task_id)
    if not task_info:
        return Response(status=404)

    return Response(data=task_info)
