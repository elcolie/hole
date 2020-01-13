from django.contrib.auth import get_user_model
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from hole.users.api.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    required_scopes = ['hole']
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [TokenHasScope, IsAuthenticated]
