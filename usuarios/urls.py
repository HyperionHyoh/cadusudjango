from django.urls import path

from .views import IndexView, UpdateUsuarioView, CreateUsuarioView, DeleteUsuarioView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', CreateUsuarioView.as_view(), name='add_usuario'),
    path('<int:pk>/update/', UpdateUsuarioView.as_view(), name='upd_usuario'),
    path('<int:pk>/delete/', DeleteUsuarioView.as_view(), name='del_usuario'),
]