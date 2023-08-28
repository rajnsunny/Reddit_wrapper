from django.urls import path
from . import views

urlpatterns = [
    path('<slug:id>', views.article_list, name='article_list'),
]
