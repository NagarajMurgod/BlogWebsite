from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateUserSerializer, UserLoginSerializer
from django.contrib.auth import authenticate, login


class SignupView(APIView):


    def post(self,request, *args, **kwargs):
     
        serialize = CreateUserSerializer(data=request.data)

        if serialize.is_valid():
            user = serialize.create(serialize.validated_data)

            return Response(serialize.data,status=status.HTTP_201_CREATED)
        
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


class SigninView(APIView):
    
    def post(self, request, *args, **kwargs):
        serialize = UserLoginSerializer(data = request.data, context={'request' : self.request})

        serialize.is_valid(raise_exception=True)
        login(request, serialize.validated_data['user'])
        return Response({
            'status' : 'sucess',
            'is_authenticated': True
        },status=status.HTTP_200_OK)

        
            # user = authenticate(request, **serializers.validated_data)
            # if user is not None:
            #     login(request, user)
            #     return Response({
            #         'status' : 'success',
            #         'is_authenticated' : True,
            #     }, status=status.HTTP_200_OK)
        

