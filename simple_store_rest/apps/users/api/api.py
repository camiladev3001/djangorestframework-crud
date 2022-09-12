from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializer import UserSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_api_view(request):
  
  if request.method == 'GET':
    users = User.objects.all()
    users_serializer = UserSerializer(users, many = True) # (many = True) ---> List of users, it expects only 1 object
    return Response(users_serializer.data)

  if request.method == 'POST':
    user_serializer = UserSerializer(data = request.data) # get json and compare to model
    if(user_serializer.is_valid()):
      user_serializer.save()
      return Response(user_serializer.data)
    
    return Response(user_serializer.errors, 400)