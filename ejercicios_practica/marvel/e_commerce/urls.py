from django.urls import path
from .api.views import comic_list_api_view, comic_retrieve_api_view, comic_create_api_view, comic_list_filtered_api_view

urlpatterns = [
    path('comic-list/', comic_list_api_view, name='comic_list_api_view'),
    path('comic-retrieve/', comic_retrieve_api_view, name='comic_retrieve_api_view'),
    path('comic-create/', comic_create_api_view, name='comic_create_api_view'),
    path('comic-list-filtered/', comic_list_filtered_api_view, name='comic_list_filtered_api_view'),
    
]




