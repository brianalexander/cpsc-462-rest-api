from djoser.serializers import UserCreateSerializer
from userauth.models import User


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password',
                  'first_name', 'last_name')
