from django.urls import path

from .views import *


urlpatterns = [
    path('', ItemsView.as_view(), name='items'),
    path('<int:pk>/', detail, name='detail'),
    path("add-item/", CreateNewItemView.as_view() , name='add-item'),
    path('<int:pk>/delete/', DeleteItem.as_view(), name="delete"),
    path('<int:pk>/edit/', UpdateItem.as_view(), name="edit"),

]
