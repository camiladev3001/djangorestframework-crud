from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.api.serializer import UserSerializer

class UserApiView(APIView):
  
  def get(self, request):
    users = User.objects.all()
    users_serializer = UserSerializer(users, many = True) # (many = True) ---> List of users, it expects only 1 object
    return Response(users_serializer.data)
