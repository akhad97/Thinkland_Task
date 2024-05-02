from rest_framework import generics 
from .models import Product
from .serializer import ProductCreateSerializer, ProductSerializer
from ..common.pagination import CustomPagination
from .documents import ProductDocument
from rest_framework import permissions
from rest_framework_simplejwt import authentication
from elasticsearch_dsl import Search
from elasticsearch_dsl import Q
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    pagination_class = CustomPagination
    # authentication_classes = [authentication.JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateSerializer
        else:
            return ProductSerializer

product_list_create_api_view = ProductListCreateAPIView.as_view()


class ProductSearch(APIView):
    serializer_class = ProductSerializer
    document_class = ProductDocument

    def generate_q_expression(self, query):
        return Q(
            "multi_match",
            query=query,
            fields=["title"],
            fuzziness="auto"
        )

    def get(self, request, query):
        q = self.generate_q_expression(query)
        search = self.document_class.search().query(q)
        return Response(self.serializer_class(search.to_queryset(), many=True).data)


product_search_api_view = ProductSearch.as_view()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

product_retrieve_update_delete_api_view = ProductDetailView.as_view()

