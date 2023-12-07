from django.urls import path, include
from .views import hello_world_view, request_data_view, get_comics, purchased_item

urlpatterns = [
    path('hello-world/', hello_world_view),
    path('request-data/', request_data_view),
    path('get-comics/', get_comics),
    path('purchased-item/', purchased_item),
    path('api/', include('e_commerce.api.urls')),  # Incluir las rutas de la API
    # Otras rutas específicas de tu aplicación e_commerce...
]





