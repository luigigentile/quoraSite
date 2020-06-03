from rest_framework.response  import Response
from rest_framework.views import APIView
from users.models import CustomUser
from users.api.serializers import  UserDisplaySerializer
from rest_framework import generics

from rest_framework.permissions import  IsAuthenticated
from questions.api.permissions import IsAuthorOrReadOnly

class CurrentUserAPIView(APIView):

    def get(self,request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)


class UsersAPIView(generics.ListAPIView):
    queryset=CustomUser.objects.all()
    serializer_class =  UserDisplaySerializer
    permissions_class = [IsAuthenticated,IsAuthorOrReadOnly]
