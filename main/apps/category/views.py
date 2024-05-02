from rest_framework import generics 
from .models import Category
from .serializer import CategoryCreateSerializer, CategorySerializer
from ..common.pagination import CustomPagination
from rest_framework import permissions
from rest_framework_simplejwt import authentication

from rest_framework import generics, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    pagination_class = CustomPagination
    serializer_class = CategorySerializer
    # authentication_classes = [authentication.JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    
    @swagger_auto_schema(
        operation_summary="List categories",
        operation_description="This endpoint allows users to list all categories.",
        responses={200: CategorySerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Create a new category",
        operation_description="This endpoint allows users to create a new category.",
        request_body=CategoryCreateSerializer,
        responses={201: CategorySerializer()}
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
category_list_create_api_view = CategoryListCreateAPIView.as_view()


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    @swagger_auto_schema(
        operation_summary="Retrieve a category",
        operation_description="This endpoint allows users to retrieve a specific category.",
        responses={200: CategorySerializer(), 404: "Not Found"}
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a category",
        operation_description="This endpoint allows users to update a specific category.",
        request_body=CategorySerializer,
        responses={200: CategorySerializer(), 400: "Bad Request"}
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a category",
        operation_description="This endpoint allows users to delete a specific category.",
        responses={204: "No Content", 404: "Not Found"}
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

category_retrieve_update_delete_api_view = CategoryDetailView.as_view()


