from .serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart

class Updatequantity(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request,cartId, format=None):
        try:
            cart_item = Cart.objects.get(id=cartId, user=request.user)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CartSerializer(cart_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST) 