from rest_framework.generics import GenericAPIView
from accounts.serializers import SignUpSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate



class SignUpAPIView(GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []


    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message" : "User Created Successfully",
                "data" : serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginAPIView(GenericAPIView):
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            response = {
                "message" : "Login Successful",
                "token" : user.auth_token.key
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message" : "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        response = {
            "id" : request.user.id,
            "username" : str(request.user.username),
            "email" : str(request.user.email),
            "auth" : str(request.auth)
        }

        return Response(data=response, status=status.HTTP_200_OK)