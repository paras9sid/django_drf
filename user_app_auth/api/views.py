# from django.shortcuts import HttpResponse
# from rest_framework.decorators import api_view
# from .serializers import RegistrationSerializer
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
# from user_app_auth import models
# from rest_framework import status



# @api_view(['POST',])
# def logout_view(request):
#     if request.method == 'POST':
#         # current logged in user - request.user
#         request.user.auth_token.delete()
#         return Response({'Successfully deleted token'},status=status.HTTP_200_OK)

# @api_view(['POST',])
# def registration_view(request):
    
#     if request.method=='POST':
#         serializer = RegistrationSerializer(data=request.data)
#         data={
            
#         }
#         if serializer.is_valid():
#             account = serializer.save()
            
#             data['response'] = 'Registration successful.'
#             data['username'] = account.username
#             data['email'] = account.email
            
#             token = Token.objects.get(user=account).key
#             data['token'] = token

            
#             # return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#         return Response(data)
        
    
        