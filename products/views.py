from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .utils import get_object
from .models import Profile, Product
from .permissions import IsEnrolled
from .serializer import product_serialize, products_serialize, user_lessons_serialize


class ProfileAPIView(APIView): 
    
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields = "__all__"  
        
    def get(self, request, id):
        profile = get_object(Profile, id=id)
        self.check_object_permissions(request, profile)
        serializer = self.OutputSerializer(profile, context={'request': request})
        return Response(serializer.data)

# 1 Задание
class AllUserProductsAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, id):
        profile = get_object(Profile, id=id)
        data = user_lessons_serialize(profile)
        # data = {}
        return Response(data)

# 2 Задание
class ProductAPIView(APIView):
    permission_classes = (IsEnrolled, )
    
    def get(self, request, id):
        product = get_object(Product, id=id)
        self.check_object_permissions(request, product)
        profile = request.user.profile
        data = product_serialize(id, profile)
        return Response(data)
        
# 3 Задание
class AllProductsAPIView(APIView):
    permission_classes = (IsAdminUser, )

    def get(self, request):
        data = products_serialize()
        return Response(data)


