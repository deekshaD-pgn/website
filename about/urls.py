from django.urls import path
from .views import contact

urlpatterns = [
   
    path('about/contact/', contact),
]
