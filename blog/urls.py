from django.urls import path
from .views import home_view, list_view

urlpatterns = [
    path('blog/', home_view, name="blog-home"),
    path('blog/list/', list_view, name="blog-list"),
]
