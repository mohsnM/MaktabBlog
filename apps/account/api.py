# Third-party imports.
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
)

from .models import User
from .permissions import HasAccess
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [HasAccess]
    queryset = User.objects.all()
    serializer_class = UserSerializer
