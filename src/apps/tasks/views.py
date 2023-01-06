from celery.result import AsyncResult
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


from .tasks import add


@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer,))
@ensure_csrf_cookie  # add csrf token to the cookie
def get_search_page(request):
    return Response(template_name='search.html')


@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer,))
@ensure_csrf_cookie  # add csrf token to the cookie
def get_task_page(request, task_id):
    return Response(template_name='task.html')


@api_view(['POST'])
def start_crawler_task(request):
    if 'url' not in request.data:
        return Response(status=400)

    task = add.delay(1, 1)

    return Response(
        data={'task_id': task.task_id}
    )


@api_view(['GET'])
def get_task_info(request, task_id):
    task = AsyncResult(str(task_id))

    return Response(
        data={
            'status': task.status,
            'result': task.result,
            'args': task.args,
        }
    )
