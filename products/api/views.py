from django.shortcuts import get_object_or_404
from core.permissions import IsOwnerOrReadOnly, IsOwnerOrForbidden
from ..models import Product
from .serializer import ProductSerializer, PublicProductSerializer


from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response


##########################################################################


class PublicProductDetail(APIView):

    def get(self, request, key, format=None):
        product = get_object_or_404(Product, key=key)
        serializer = PublicProductSerializer(product)
        return Response(serializer.data)


class PrivateProductDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsListView(generics.ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = self.request.user.products.all()
        return queryset




