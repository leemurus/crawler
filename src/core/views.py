from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.request import Request


@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer,))
def page_not_found_view(request: Request, exception):
    return Response(template_name='404.html', status=404)
