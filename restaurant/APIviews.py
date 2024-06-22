from .serializers import CartSerializer,FeedbackSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart,Feedback,Item

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

class FeedbackSubmission(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        feedback = request.data
        user = request.user
        item_id = int(feedback['itemid'])
        item = Item.objects.get(id = item_id)
        rating = feedback['rating']
        experience = feedback['experience']
       
        item_rating = item.item_rating
        people = item.people_rated
        item_rating = ((item_rating*people)+rating)/(people+1)
        people += 1
        item.item_rating = item_rating
        item.people_rated = people
        item.save()

        item_feedback = Feedback(
           user = user,
           item = item,
           rating=rating,
           experience=experience
        )
        item_feedback.save()
        return Response(status=status.HTTP_200_OK)
        

