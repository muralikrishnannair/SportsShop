from rest_framework import serializers
from SportsApp.models import CategoryDb,ProductDb


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=CategoryDb
        fields='__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=ProductDb
        fields='__all__'