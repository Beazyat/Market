from django.urls import path

from .views import *


urlpatterns = [
    path('<int:pk>/', detail, name='detail'),
    path("add-item/", CreateNewItemView.as_view() , name='add-item'),
]
