from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import RegistrationSerializer
from user_app_auth import models


@api_view(['POST',])
def registration_view(request):
    
    if request.method=='POST':
        serializer = RegistrationSerializer(data=request.data)

        #store everything inside it 
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            
            # storing below data in dict format which is initialized empty at start
            # will be seen in response after post rq for registration
            data['response'] = "Registartion successful..."
            data['username'] = account.username
            data['email'] = account.email

            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors

        return Response(data)