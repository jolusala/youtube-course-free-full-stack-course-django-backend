from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from products.models import ProductCategory, Maker, Product

from products.serializers import (
    MakerSerializer,
    ProductSerializer,
    ProductCategorySerializer,
)

# Create your views here.


class ProductCategoryListView(ListCreateAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()


class MakerListView(ListCreateAPIView):
    serializer_class = MakerSerializer
    queryset = Maker.objects.all()


class ProductsListView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
