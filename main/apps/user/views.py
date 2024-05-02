# from rest_framework import permissions
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .serializer import (
#     UserRegistrationSerializer,
#     UserLoginSerializer,
#     UserDetailSerializer
# )
# from rest_framework.response import Response
# from rest_framework import generics, status
# from django.contrib.auth import get_user_model
# from django.utils.translation import gettext_lazy as _
# from rest_framework.renderers import JSONRenderer


# User = get_user_model()



# class AuthUserRegistrationView(generics.GenericAPIView):
#     serializer_class = UserRegistrationSerializer
#     queryset = User.objects.all()
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         valid = serializer.is_valid(raise_exception=True)
#         if valid:
#             serializer.save()
#         status_code = status.HTTP_201_CREATED 
#         response = {
#             'success': True,
#             'statusCode': status_code,
#             'message': 'User succesfully registered',
#             'user': serializer.data
#         }
#         return Response(response, status=status_code)


# user_registration_api_view = AuthUserRegistrationView.as_view()


# class CustomRenderer(JSONRenderer):
#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         if renderer_context is not None:
#             if 'success' not in data:
#                 data['success'] = True
#         return super().render(data, accepted_media_type, renderer_context)


# class UserLoginView(TokenObtainPairView):
#     permission_classes = (permissions.AllowAny,)
#     serializer_class = UserLoginSerializer
#     renderer_classes = (CustomRenderer,)

#     def get(self, request, *args, **kwargs):
#         try:
#             response = super().get(request, *args, **kwargs)
#             return response
#         except Exception as e:
#             return Response({'success': False, 'error': str(e)})


# user_login_api_view = UserLoginView().as_view()


# class UserDetailAPIView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserDetailSerializer
#     lookup_field = "guid"


# user_detail_api_view = UserDetailAPIView.as_view()


from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import UserRegistrationSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth.models import User



class AuthUserRegistrationView(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            serializer.save()
        status_code = status.HTTP_201_CREATED 
        response = {
            'success': True,
            'statusCode': status_code,
            'message': 'User succesfully registered',
            'user': serializer.data
        }
        return Response(response, status=status_code)


user_registration_api_view = AuthUserRegistrationView.as_view()


class UserLoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer

    def get(self, request, *args, **kwargs):
        try:
            response = super().get(request, *args, **kwargs)
            return response
        except Exception as e:
            return Response({'success': False, 'error': str(e)})


user_login_api_view = UserLoginView().as_view()

