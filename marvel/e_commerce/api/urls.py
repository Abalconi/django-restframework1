from django.urls import path
from e_commerce.api.views import ComicListAPIView, ComicRetrieveAPIView, ComicCreateAPIView

urlpatterns = [
    path('comic-list/', ComicListAPIView.as_view(), name='comic_list_api_view'),
    path('comic-retrieve/', ComicRetrieveAPIView.as_view(), name='comic_retrieve_api_view'),
    path('comic-create/', ComicCreateAPIView.as_view(), name='comic_create_api_view')
]