from product.models import Category, ImageUpload, OrderItem,  Product
from rest_framework.views import APIView  
from rest_framework.parsers import FormParser,  MultiPartParser
from .serializers import ( ImageUploadSerializer, OrderItemSerializer,
                            ProductSerializer,
                            CategorySerializer
                        )
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from nepali_unicode_converter.convert import Converter

# Create your views here.
class ImageUploadView(APIView):
    parsers = (FormParser,MultiPartParser)

    def post(self,request,*args,**kwargs):
        file_seriailzer = ImageUploadSerializer(data=request.data)
        if(file_seriailzer.is_valid()):
            file_seriailzer.save()
            return Response(file_seriailzer.data,status=status.HTTP_200_OK)
        else:
            return Response(file_seriailzer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class=CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class= CategorySerializer

class ImageUploadListView(generics.ListCreateAPIView):
    parsers = (FormParser,MultiPartParser)
    queryset = ImageUpload.objects.all()
    serializer_class=ImageUploadSerializer

class OrderItemView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer