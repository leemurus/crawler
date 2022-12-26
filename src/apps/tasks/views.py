from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer,))
def index(request):
    return Response(template_name='index.html')


@api_view(['POST'])
@renderer_classes((TemplateHTMLRenderer,))
def start_search(request):
    return Response(template_name='index.html')
