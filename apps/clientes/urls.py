from django.urls import path
from .views import ClienteCreate, ClientesList, ClientesUpdate, ClienteDelete

urlpatterns = [
    path('', ClientesList.as_view(), name='clientes_lista'),
    path('novo/', ClienteCreate.as_view(), name='create_cliente'),
    path('editar/<int:pk>', ClientesUpdate.as_view(), name='update_cliente'),
    path('deletar/<int:pk>', ClienteDelete.as_view(), name='delete_cliente'),
]
