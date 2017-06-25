from django.contrib.auth.models import User
from rest_framework.decorators import detail_route
from words.models import Expression, Group
from rest.serializers.user_serializers import UserSerializer
from rest.serializers.words_serializers import ExpressionSerializer, GroupSerializer
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):

    serializer_class = GroupSerializer
    # queryset = Group.objects.all()

    def get_queryset(self):
        return Group.objects.filter(user=self.request.user)


class ExpressionViewSet(viewsets.ModelViewSet):

    serializer_class = ExpressionSerializer
    # queryset = Expression.objects.all()

    def get_queryset(self):
        return Expression.objects.filter(groups__user=self.request.user)

