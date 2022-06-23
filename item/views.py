from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import item
from .serializers import CategorySerializer,ItemSerilizer
from .models import Category

# Create your views here.

class ItemView(APIView):
    def get(self, request):
        cate_name = request.data.get('category','')
        category = Category.objects.get(name=cate_name)
        return Response(CategorySerializer(category).data,status = status.HTTP_200_OK)
    def post(self,request):
        item_serializer = ItemSerilizer(data = request.data)
        item_serializer.is_valid(raise_exception=True)
        print('?')
        item_serializer.save()
        return Response(item_serializer.data, status=status.HTTP_200_OK)