from django.urls import path
from .views import start_search, index

urlpatterns = [
    path('', index),
    path('/tasks', start_search),
]