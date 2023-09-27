from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from .utils import get_object
from .models import Profile, Product
from .permissions import IsEnrolled, IsProfileOwner
from .serializer import product_serialize, products_serialize, user_lessons_serialize


# 1 Задание
class UserProductsAPIView(APIView):
    permission_classes = ((IsAdminUser|IsProfileOwner),)

    def get(self, request, id):
        profile = get_object(Profile, id=id)
        self.check_object_permissions(request, profile)
        data = user_lessons_serialize(profile)
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


