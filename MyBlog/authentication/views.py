from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateUserSerializer

class SignupView(APIView):


    def post(self,request, *args, **kwargs):
        serialize = CreateUserSerializer(data=request.data)

        if serialize.is_valid():
            user = serialize.create(serialize.validated_data)

            return Response(serialize.data,status=status.HTTP_201_CREATED)
        
        return Response(serialize.error, status=status.HTTP_400_BAD_REQUEST)
            
