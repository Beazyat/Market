from django.urls import path

from .views import new_conversation, inbox, detail

urlpatterns = [
    path('inbox/', inbox, name="inbox"),
    path('new/<int:item_pk>/', new_conversation, name="new"),
    path('<int:pk>/', detail, name="conversation-detail"),

]
