from django.urls import path
from . import views


urlpatterns = [
    path(
        "", 
        views.category_list_create_api_view,
        name='category_list_create'
    ),
    path(
        "<uuid:guid>/", 
        views.category_retrieve_update_delete_api_view, 
        name="category_detail_update_delete"
    )
]

