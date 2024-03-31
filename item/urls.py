from django.urls import path

from .views import detail


urlpatterns = [
    path('<int:pk>/', detail, name='detail'),
]
