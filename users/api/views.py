# users/api/views.py

# rest_framework
from rest_framework          import generics
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens      import AccessToken

# local
from users.api.serializers import RegisterSerializer


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token_read   = TokenObtainPairSerializer().get_token(user)
        token_access = AccessToken().for_user(user)

        return Response({
            "access_token" : str(token_access)
        })
