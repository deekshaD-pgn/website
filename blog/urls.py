from django.urls import path
from .views import list_view

urlpatterns = [
    path('blog/list/', list_view),
]
