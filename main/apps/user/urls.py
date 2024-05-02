from django.urls import path
from . import views


urlpatterns = [
    path(
        'register/', 
        views.user_registration_api_view, 
        name='register'
    ),
    path(
        'login/', 
        views.user_login_api_view, 
        name='login'
    ),
    # path(
    #     "<uuid:guid>/detail/", 
    #     views.user_detail_api_view, 
    #     name="user_detail"
    # )
]
