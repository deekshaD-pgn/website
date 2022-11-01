from django.urls import path
from .views import home_view, list_view, CreateView, DeleteView

urlpatterns = [
    path('blog/', home_view, name="blog-home"),
    path('blog/list/', list_view, name="blog-list"),
    path('blog/add/', CreateView.as_view(), name="blog-add"),
    path('blog/del/', DeleteView.as_view(), name="blog-del"),
 ]

