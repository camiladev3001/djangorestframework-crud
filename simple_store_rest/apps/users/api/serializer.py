from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    # fields = ['name', 'last_name', '...']

class TestUserSerializer(serializers.Serializer):
  name = serializers.CharField(max_length = 200)
  email = serializers.EmailField()
  age = serializers.CharField(max_length = 2)

  def validate_name(self, value):

    # custom validation
    if 'developer' in value:
      raise serializers.ValidationError('no puede existir un usuario con ese nombre', 'Invalid')
    return value

  def validate_email(self, value):
    if value == '':
      raise serializers.ValidationError('Tiene que indicar un correo')

    # it is just an if
    # if self.context['name'] in value:
      # raise serializers.ValidationError('El email no puede contener el nombre')

    if self.validate_name(self.context['name']) in value:
      raise serializers.ValidationError('El email no puede contener el nombre')

    return value

  def validate_age(self, value):
    return value
  
  def validate(self, data):
    # if data['name'] in data['email']:
      # raise serializers.ValidationError('El email no puede contener el nombre')

    return data