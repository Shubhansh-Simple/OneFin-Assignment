# users/api/serializers.py

# rest_framework
from rest_framework import serializers

# local
from ..models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CustomUser
        fields = ('id','username','password',)
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

    def create(self,validated_data):
        user = CustomUser.objects.create_user(validated_data['username'], password=validated_data['password'])
        return user





