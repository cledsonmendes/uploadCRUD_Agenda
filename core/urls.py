from django.urls import path
from .views import IndexView, CreateContatoView, UpdateContatoView, DeleteContatoView, DetailContatoView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', CreateContatoView.as_view(), name='add_contato'),
    path('<int:pk>/update/', UpdateContatoView.as_view(), name='upd_contato'),
    path('<int:pk>/delete/', DeleteContatoView.as_view(), name='del_contato'),
    path('<int:pk>/info/', DetailContatoView.as_view(), name='info_contato'),
]
