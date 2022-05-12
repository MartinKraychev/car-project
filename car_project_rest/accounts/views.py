from django.contrib.auth import get_user_model

from rest_framework import mixins, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from car_project_rest.accounts.serializers import RegisterSerializer

UserModel = get_user_model()


class LoginView(ObtainAuthToken):
    permission_classes = (
        AllowAny,
    )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
        })


class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = UserModel.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (
        AllowAny,
    )


