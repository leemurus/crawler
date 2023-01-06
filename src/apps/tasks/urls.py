from django.urls import path
from .views import (
    get_task_info,
    start_crawler_task,
    get_search_page,
    get_task_page
)

urlpatterns = [
    # html pages
    path('', get_search_page),
    path('task/<uuid:task_id>', get_task_page),

    # api urls
    path('api/task', start_crawler_task),
    path('api/task/<uuid:task_id>', get_task_info),
]