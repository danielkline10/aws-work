from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairUserTypeView, CustomUserCreate
from .views import HelloWorldView
urlpatterns = [
    # api to obtain token
    path('token/obtain/', ObtainTokenPairUserTypeView.as_view(),
         name='token_create'),  # override sjwt stock token



    # api to refresh token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),

    # api to create user
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),

    # api to test out the helloworld
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
]
