from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

import uuid


@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer,))
def get_search_page(request):
    return Response(template_name='search.html')


@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer,))
def get_task_page(request, task_id):
    print(f'get_task_page {task_id}')

    return Response(template_name='task.html')


@api_view(['POST'])
def start_crawler_task(request):
    if 'url' not in request.data:
        return Response(status=400)

    task_id = uuid.uuid4()
    return Response(
        data={'task_id': task_id}
    )


@api_view(['GET'])
def get_task_info(request, task_id):
    print(f'api/get_task_info {task_id}')

    return Response(
        data={'status': 'processing'}
    )


