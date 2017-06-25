from rest.serializers.words_serializers import ExpressionSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from words.models import Expression, Group
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework import generics


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_group_expressions(request, group_id, format=None):
    group = Group.objects.filter(user=request.user, pk=group_id).first()
    expressions = Expression.objects.filter(groups=group)
    serializer = ExpressionSerializer(expressions, many=True, context={'request': request})
    return Response(serializer.data)


class ExpressionList(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):

    queryset = Expression.objects.all()
    serializer_class = ExpressionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
