from rest_framework.decorators import api_view
from rest_framework.response import Response
from words.views_examination import init_test, get_next_expression
from rest.serializers.words_serializers import ExpressionSerializer


@api_view(['GET', 'POST'])
def start_test(request, group_id):
    result = init_test(request, group_id)
    if 'error' in result:
        return Response(result)

    expression = result['expression']
    serializer = ExpressionSerializer(expression)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def get_next(request):
    expression = get_next_expression(request)
    if expression is None:
        content = {'end_of_test': True}
        return Response(content)

    serializer = ExpressionSerializer(expression)
    return Response(serializer.data)

