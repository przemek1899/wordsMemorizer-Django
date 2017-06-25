from rest_framework import serializers
from words.models import Expression, Group


class ExpressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expression
        exclude = ('groups', 'image')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('name', 'parent')

